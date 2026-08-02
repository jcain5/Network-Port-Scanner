import unittest
import argparse

from main import positive_timeout

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


if __name__ == "__main__":
    unittest.main()