#!/usr/bin/python3
"""Unittests for the max_integer function.

These tests cover empty lists, single values, and several orderings.
"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_empty_list(self):
        """An empty list has no maximum."""
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        """A single-element list returns that element."""
        self.assertEqual(max_integer([7]), 7)

    def test_ascending_order(self):
        """The maximum is the last value when values ascend."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_descending_order(self):
        """The maximum is the first value when values descend."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_mixed_order(self):
        """The maximum is found anywhere in the list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_values(self):
        """The maximum of negative values is the least negative."""
        self.assertEqual(max_integer([-5, -1, -9]), -1)

    def test_duplicate_maximum(self):
        """Repeated maximum values are handled correctly."""
        self.assertEqual(max_integer([4, 4, 1, 4]), 4)


if __name__ == "__main__":
    unittest.main()
