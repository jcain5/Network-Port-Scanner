import socket
import unittest
from unittest.mock import patch

from scanner.scanning import scan_port, scan_udp_port, scan_host, encode_dns_name, build_dns_query, summarize_results


class TestScanPort(unittest.TestCase):
    @patch("scanner.scanning.socket.create_connection")
    def test_open_port(self, mock_connection) -> None:
        mock_connection.return_value.__enter__.return_value

        result = scan_port("192.0.2.10", 443)

        self.assertEqual(result, "OPEN")

    
    @patch("scanner.scanning.socket.create_connection")
    def test_closed_port(self, mock_connection) -> None:
        mock_connection.side_effect = ConnectionRefusedError

        result = scan_port("192.0.2.10", 443)

        self.assertEqual(result, "CLOSED")


    @patch("scanner.scanning.socket.create_connection")
    def test_timeout(self, mock_connection) -> None:
        mock_connection.side_effect = socket.timeout

        result = scan_port("192.0.2.10", 443)

        self.assertEqual(result, "TIMEOUT")


    @patch("scanner.scanning.socket.create_connection")
    def test_unreachable(self, mock_connection) -> None:
        mock_connection.side_effect = OSError

        result = scan_port("192.0.2.10", 443)

        self.assertEqual(result, "UNREACHABLE")


class TestScanUDPPort(unittest.TestCase):
    @patch("scanner.scanning.socket.socket")
    def test_udp_open(self, mock_socket) -> None:
        mock_sock = mock_socket.return_value.__enter__.return_value
        mock_sock.recvfrom.return_value = (
            b"response",
            ("192.0.2.10", 53)
        )
        result = scan_udp_port(
            "192.0.2.10",
            53,
            timeout=0.5,
        )
        self.assertEqual(result, "OPEN")

    @patch("scanner.scanning.socket.socket")
    def test_udp_timeout(self, mock_socket) -> None:
        mock_sock = mock_socket.return_value.__enter__.return_value
        mock_sock.recvfrom.side_effect = socket.timeout

        result = scan_udp_port(
            "192.0.2.10",
            53,
            timeout=0.5,
        )

        self.assertEqual(result, "OPEN|FILTERED")


    @patch("scanner.scanning.socket.socket")
    def test_udp_closed(self, mock_socket) -> None:
        mock_sock = mock_socket.return_value.__enter__.return_value
        mock_sock.recvfrom.side_effect = ConnectionRefusedError

        result = scan_udp_port(
            "192.0.2.10",
            53,
            timeout=0.5,
        )

        self.assertEqual(result, "CLOSED")

    @patch("scanner.scanning.socket.socket")
    def test_udp_unreachable(self, mock_socket) -> None:
        mock_sock = mock_socket.return_value.__enter__.return_value
        mock_sock.recvfrom.side_effect = OSError
        result = scan_udp_port(
            "192.0.2.10",
            53,
            timeout=0.5,
        )

        self.assertEqual(result, "UNREACHABLE")


    @patch("scanner.scanning.scan_udp_port")
    def test_scan_host_uses_udp(self, mock_scan_udp_port) -> None:
        mock_scan_udp_port.return_value = "OPEN"

        result = scan_host(
            "192.0.2.10",
            {53: "DNS"},
            timeout=0.5,
            protocol="udp",
        )

        mock_scan_udp_port.assert_called_with(
            "192.0.2.10",
            53,
            0.5,
        )

        self.assertEqual(
            result[0]["status"],
            "OPEN",
        )

    @patch("scanner.scanning.socket.socket")
    def test_udp_uses_dns_payload(self, mock_socket) -> None:
        mock_sock = mock_socket.return_value.__enter__.return_value

        mock_sock.recvfrom.return_value = (
            b"dns-response",
            ("192.0.2.10", 53),
        )

        result = scan_udp_port(
            "192.0.2.10",
            53,
            timeout=0.5,
        )

        expected_payload = build_dns_query("example.com")

        mock_sock.sendto.assert_called_with(
            expected_payload,
            ("192.0.2.10", 53),
        )

class TestDnsHelpers(unittest.TestCase):
    def test_encode_dns_name(self) -> None:
        result = encode_dns_name("example.com")

        self.assertEqual(
            result,
            b"\x07example\x03com\x00"
        )


    def test_build_dns_query(self) -> None:
        result = build_dns_query("example.com")

        self.assertTrue(result.startswith(b"\x12\x34"))
        self.assertIn(
            b"\x07example\x03com\x00",
            result,
        )

        self.assertTrue(result.endswith(b"\x00\x01\x00\x01"))

class TestSummarizeResults(unittest.TestCase):
    def test_counts_statuses(self) -> None:
        results = [
            {"status": "OPEN"},
            {"status": "OPEN"},
            {"status": "CLOSED"},
            {"status": "TIMEOUT"},
        ]

        summary = summarize_results(results)

        self.assertEqual(
            summary,
            {
                "OPEN": 2,
                "CLOSED": 1,
                "TIMEOUT": 1,
            }
        )

if __name__ == "__main__":
    unittest.main()