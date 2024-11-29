#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """unittest max_integer"""
    def test_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_reverse_list(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_middle_list(self):
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)

    def test_same_list(self):
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)

    def test_negative_number(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_float_list(self):
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)

    def test_one_element_list(self):
        self.assertEqual(max_integer([1]), 1)

    def test_string(self):
        self.assertEqual(max_integer(["Zamdane"]), "Zamdane")

    def test_empty_list(self):
        self.assertIsNone(max_integer([]), None)
