#!/usr/bin/python3
"""Unittest for the Rectangle class.
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Tests for the Rectangle class."""

    def test_is_base_subclass(self):
        """Test that Rectangle inherits from Base."""
        r = Rectangle(10, 2)
        self.assertIsInstance(r, Base)

    def test_basic_attributes(self):
        """Test width, height, x, y are correctly assigned."""
        r = Rectangle(10, 2, 1, 3)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 3)

    def test_default_x_y(self):
        """Test x and y default to 0."""
        r = Rectangle(10, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_id_assigned(self):
        """Test explicit id assignment."""
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r.id, 12)

    def test_width_type_error(self):
        """Test width raises TypeError on non-integer."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(10, "2")

    def test_height_type_error(self):
        """Test height raises TypeError on non-integer."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle("10", 2)

    def test_width_value_error(self):
        """Test width raises ValueError when <= 0."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 2)

    def test_height_value_error(self):
        """Test height raises ValueError when <= 0."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0)

    def test_x_type_error(self):
        """Test x raises TypeError on non-integer."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, {}, 0)

    def test_y_value_error(self):
        """Test y raises ValueError when < 0."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -1)

    def test_area(self):
        """Test area calculation."""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_str(self):
        """Test the __str__ representation."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_args(self):
        """Test update with no-keyword arguments."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        """Test update with keyword arguments."""
        r = Rectangle(10, 10, 10, 10)
        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r), "[Rectangle] (1) 1/3 - 4/2")

    def test_to_dictionary(self):
        """Test to_dictionary returns the correct dict."""
        r = Rectangle(10, 2, 1, 9, 5)
        expected = {"id": 5, "width": 10, "height": 2, "x": 1, "y": 9}
        self.assertEqual(r.to_dictionary(), expected)

    def test_to_dictionary_type(self):
        """Test to_dictionary returns a dict instance."""
        r = Rectangle(10, 2)
        self.assertIsInstance(r.to_dictionary(), dict)


if __name__ == "__main__":
    unittest.main()
