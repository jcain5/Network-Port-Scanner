import socket
import unittest
from unittest import result
from unittest.mock import patch

from scanner.scanning import scan_port



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


        if __name__ == "__main__":
            unittest.main()