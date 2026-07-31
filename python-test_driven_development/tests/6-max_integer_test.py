#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function."""

    def test_ordered_list(self):
        """Test with an already ordered list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_no_argument(self):
        """Test with no argument given (uses default)."""
        self.assertEqual(max_integer(), None)

    def test_one_element(self):
        """Test with a list containing one element."""
        self.assertEqual(max_integer([5]), 5)

    def test_negative_numbers(self):
        """Test with a list of negative numbers."""
        self.assertEqual(max_integer([-1, -5, -3]), -1)

    def test_mixed_positive_negative(self):
        """Test with a mix of positive and negative numbers."""
        self.assertEqual(max_integer([-1, 5, -3, 2]), 5)

    def test_all_same_elements(self):
        """Test with a list where all elements are the same."""
        self.assertEqual(max_integer([7, 7, 7]), 7)

    def test_floats(self):
        """Test with a list of floats."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_max_at_start(self):
        """Test where the max value is the first element."""
        self.assertEqual(max_integer([10, 1, 2, 3]), 10)

    def test_max_at_end(self):
        """Test where the max value is the last element."""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)


if __name__ == "__main__":
    unittest.main()
