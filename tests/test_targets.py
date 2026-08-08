import unittest

from scanner.targets import expand_targets

class TestExpandTargets(unittest.TestCase):

    def test_single_ipv4_address(self) -> None:
        result = expand_targets("192.168.0.2")
        self.assertEqual(result, ["192.168.0.2"])


    def test_single_ipv6_address(self) -> None:
        result = expand_targets("2001:dba::1")
        self.assertEqual(result, ["2001:dba::1"])


    def test_ipv4_cidr(self) -> None:
        result = expand_targets("192.168.1.0/30")
        self.assertEqual(result, ["192.168.1.1" , "192.168.1.2"])


    def test_invalid_target(self) -> None:
        with self.assertRaises(ValueError):
            expand_targets("not-an-ip")


    def test_cidr_above_host_limit(self) -> None:
        with self.assertRaises(ValueError):
            expand_targets("10.0.0.0/16")

    def test_ipv4_32_cidr(self) -> None:
        result = expand_targets("192.168.1.5/32")
        self.assertEqual(result, ["192.168.1.5"])

    def test_ipv4_31_cidr(self) -> None:
        result = expand_targets("192.168.1.0/31")
        self.assertEqual(result , ["192.168.1.0" , "192.168.1.1"])
if __name__ == "__main__":
    unittest.main()