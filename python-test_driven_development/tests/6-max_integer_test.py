#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_max_integer(self):
        # Test with a list of integers
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([0, -1, -2, -3]), 0)
        self.assertEqual(max_integer([100, 200, 300, 50]), 300)

    def test_empty_list(self):
        # Test with an empty list
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        # Test with a list containing a single element
        self.assertEqual(max_integer([10]), 10)

    def test_non_integer(self):
        # Test with non-integer values (should raise an exception)
        with self.assertRaises(TypeError):
            max_integer([1, 2, "three", 4])
        with self.assertRaises(TypeError):
            max_integer("not a list")
        with self.assertRaises(TypeError):
            max_integer([None, 1, 2, 3])

if __name__ == '__main__':
    unittest.main()

