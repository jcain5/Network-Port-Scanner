import unittest
import argparse

from main import parse_ports, positive_timeout

class TestPositiveTimeout(unittest.TestCase):
    def test_valid_integer(self) -> None:
        self.assertEqual(positive_timeout("1"), 1)


    def test_valid_decimal_timeout(self) -> None:
        self.assertEqual(positive_timeout("0.5"), 0.5)


    def test_zero_timeout(self) -> None:
        with self.assertRaises(argparse.ArgumentTypeError):
            positive_timeout("0")


    def test_negative_timeout(self) -> None:
        with self.assertRaises(argparse.ArgumentTypeError):
            positive_timeout("-1")


    def test_timeout_above_maximum(self) -> None:
        with self.assertRaises(argparse.ArgumentTypeError):
            positive_timeout("61")


    def test_non_numeric_timeout(self) -> None:
        with self.assertRaises(argparse.ArgumentTypeError):
            positive_timeout("banana")


class TestParsePorts(unittest.TestCase):

    def test_valid_ports(self) -> None:
        self.assertEqual(
            parse_ports("22,80,443"),
            [22, 80, 443],
        )

    def test_ports_with_spaces(self) -> None:
        self.assertEqual(
            parse_ports("22, 80, 443"),
            [22, 80, 443],
        )

    def test_single_port(self) -> None:
        self.assertEqual(
            parse_ports("3389"),
            [3389],
        )

    def test_non_numeric_port(self) -> None:
        with self.assertRaises(argparse.ArgumentTypeError):
            parse_ports("22,banana,443")

    def test_port_below_range(self) -> None:
        with self.assertRaises(argparse.ArgumentTypeError):
            parse_ports("0,443")

    def test_port_above_range(self) -> None:
        with self.assertRaises(argparse.ArgumentTypeError):
            parse_ports("22,65536")

if __name__ == "__main__":
    unittest.main()