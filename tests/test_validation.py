import unittest
from scanner.validation import validate_ip

class TestValidateIP(unittest.TestCase):


    def test_valid_ipv4_address(self) -> None:
        self.assertTrue(validate_ip("127.0.0.1"))


    def test_valid_ipv4_address(self) -> None:
        self.assertTrue(validate_ip("172.16.10.1"))


    def test_invalid_ipv4_address(self) -> None:
        self.assertFalse(validate_ip("999.1.1.1"))


    def test_non_ip_text(self) -> None:
        self.assertFalse(validate_ip("not-an-ip"))
        

    def test_valid_ipv6_address(self) -> None:
        self.assertTrue(validate_ip("2001:db8::1"))




if __name__ == "__main__":
    unittest.main()