#!/usr/bin/python3
"""Unittest for the Base class.
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests for the Base class."""

    def test_id_assigned_if_given(self):
        """Test that a given id is assigned directly."""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_auto_incremented(self):
        """Test that ids auto-increment when none is given."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_none_explicit(self):
        """Test passing id=None explicitly still auto-increments."""
        b1 = Base()
        b2 = Base(id=None)
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_is_integer(self):
        """Test that the id attribute is an integer."""
        b = Base()
        self.assertIsInstance(b.id, int)

    def test_negative_id(self):
        """Test that a negative id is accepted as given."""
        b = Base(-5)
        self.assertEqual(b.id, -5)


if __name__ == "__main__":
    unittest.main()
