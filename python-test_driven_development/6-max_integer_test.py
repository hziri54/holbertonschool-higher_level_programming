#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class for testing the max_integer function"""

    def test_max_integer(self):
        """Test for normal cases"""

        # Test with a normal list of positive integers
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

        # Test with a list of mixed integers
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

        # Test with a list of negative integers
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

        # Test with a list containing both positive and negative numbers
        self.assertEqual(max_integer([-1, 2, 3, -4]), 3)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_single_element(self):
        """Test with a list containing one element"""
        self.assertEqual(max_integer([5]), 5)

    def test_identical_elements(self):
        """Test with a list of identical elements"""
        self.assertEqual(max_integer([7, 7, 7]), 7)

    def test_large_numbers(self):
        """Test with a list of very large numbers"""
        self.assertEqual(max_integer([1000000000, 2000000000, 3000000000]), 3000000000)

    def test_floats(self):
        """Test with a list of floats"""
        self.assertEqual(max_integer([1.1, 2.2, 3.3]), 3.3)

if __name__ == "__main__":
    unittest.main()
