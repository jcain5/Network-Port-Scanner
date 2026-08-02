import unittest
import argparse

from main import parse_arguments, parse_ports, positive_timeout

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


class TestArgumentParser(unittest.TestCase):
    def test_required_target(self) -> None:
        args = parse_arguments([
            "--target",
            "192.0.2.10",
        ])

        self.assertEqual(args.target, "192.0.2.10")


    def test_default_timeout(self) -> None:
        args = parse_arguments([
            "--target",
             "192.0.2.10",
        ])

        self.assertEqual(args.timeout, 1.0)


    def test_default_output(self) -> None:
        args = parse_arguments([
            "--target",
            "192.0.2.10",
        ])

        self.assertEqual(args.output, "scan_results.csv")


    def test_default_file_mode(self) -> None:
        args = parse_arguments([
            "--target",
            "192.0.2.10",
        ])

        self.assertEqual(args.file_mode, "a")


    def test_custom_argumnets(self) -> None:
        args = parse_arguments([
            "--target",
            "192.0.2.10",
            "--timeout",
            "0.5",
            "--ports",
            "22,80,443",
            "--output",
            "sample.csv",
            "--overwrite",
        ])

        self.assertEqual(args.target, "192.0.2.10")
        self.assertEqual(args.timeout, 0.5)
        self.assertEqual(args.ports, [22, 80, 443])
        self.assertEqual(args.output, "sample.csv")
        self.assertEqual(args.file_mode, "w")


    def test_conflicting_file_mode(self) -> None:
        with self.assertRaises(SystemExit):
            parse_arguments([
            "--target",
            "192.0.2.10",
            "--append",
            "--overwrite",
            ])


    def test_missing_target(self) -> None:
        with self.assertRaises(SystemExit):
            parse_arguments([])