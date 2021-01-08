#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define function to test max_integer function"""

    def test_max_integer(self):
        """Test success Cases"""

        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([2, 2, 2]), 2)
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([3, 2, 1]), 3)
        self.assertEqual(max_integer([2, 3, 1]), 3)
        self.assertEqual(max_integer([-8, -90, -1]), -1)
        self.assertEqual(max_integer([0.1, 0.5, 0.04]), 0.5)

if __name__ == "__main__":
    unittest.main()
