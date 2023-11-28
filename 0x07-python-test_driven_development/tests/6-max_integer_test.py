#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer([..])"""
    def test1(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([1]), 1)

    def test_empty_list(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([]), None)

    def test2(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([9, 1, 5, 3]), 9)

    def test3(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([-1, -4, -9, -8]), -1)

    def test4(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([1.5, 1.6, 3.9, 8.60, 9.99]), 9.99)

    def test5(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer(), None)

    def test_str_list(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer([["bro"], ["do"], ["abc"], ["sic"], ["ric"]]),
            ["sic"])

    def test_float(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer(9.8)


if __name__ == '__main__':
    unittest.main()
