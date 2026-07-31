#!/usr/bin/python3
"""Unittest for the Square class.
"""
import unittest
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """Tests for the Square class."""

    def test_is_rectangle_subclass(self):
        """Test that Square inherits from Rectangle."""
        s = Square(5)
        self.assertIsInstance(s, Rectangle)

    def test_width_height_equal(self):
        """Test width and height are equal to size."""
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

    def test_default_x_y(self):
        """Test x and y default to 0."""
        s = Square(5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_area(self):
        """Test area calculation."""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_str(self):
        """Test the __str__ representation."""
        s = Square(3, 1, 3, 5)
        self.assertEqual(str(s), "[Square] (5) 1/3 - 3")

    def test_size_getter(self):
        """Test the size property getter."""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_setter(self):
        """Test the size property setter updates width and height."""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_size_setter_type_error(self):
        """Test size setter raises TypeError on non-integer."""
        s = Square(5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.size = "9"

    def test_update_args(self):
        """Test update with no-keyword arguments."""
        s = Square(5)
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

    def test_update_kwargs(self):
        """Test update with keyword arguments."""
        s = Square(5)
        s.update(size=7, id=89, y=1)
        self.assertEqual(str(s), "[Square] (89) 0/1 - 7")

    def test_to_dictionary(self):
        """Test to_dictionary returns the correct dict."""
        s = Square(10, 2, 1, 5)
        expected = {"id": 5, "size": 10, "x": 2, "y": 1}
        self.assertEqual(s.to_dictionary(), expected)

    def test_to_dictionary_type(self):
        """Test to_dictionary returns a dict instance."""
        s = Square(5)
        self.assertIsInstance(s.to_dictionary(), dict)


if __name__ == "__main__":
    unittest.main()
