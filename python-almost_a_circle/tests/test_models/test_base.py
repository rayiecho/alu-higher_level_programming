#!/usr/bin/python3
"""Unittest for the Base class.
"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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

    def test_id_is_integer(self):
        """Test that the id attribute is an integer."""
        b = Base()
        self.assertIsInstance(b.id, int)


class TestToJsonString(unittest.TestCase):
    """Tests for Base.to_json_string."""

    def test_none_returns_empty_list_string(self):
        """Test None input returns '[]'."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_empty_list_returns_empty_list_string(self):
        """Test empty list input returns '[]'."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_valid_list(self):
        """Test a valid list of dictionaries is converted correctly."""
        result = Base.to_json_string([{"id": 1}])
        self.assertEqual(result, '[{"id": 1}]')

    def test_returns_string_type(self):
        """Test the return type is a string."""
        self.assertIsInstance(Base.to_json_string([{"id": 1}]), str)


class TestFromJsonString(unittest.TestCase):
    """Tests for Base.from_json_string."""

    def test_none_returns_empty_list(self):
        """Test None input returns an empty list."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_empty_string_returns_empty_list(self):
        """Test empty string input returns an empty list."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_valid_json_string(self):
        """Test a valid JSON string is parsed correctly."""
        result = Base.from_json_string('[{"id": 1}]')
        self.assertEqual(result, [{"id": 1}])

    def test_returns_list_type(self):
        """Test the return type is a list."""
        self.assertIsInstance(Base.from_json_string('[{"id": 1}]'), list)


class TestSaveToFile(unittest.TestCase):
    """Tests for Base.save_to_file."""

    def tearDown(self):
        """Clean up any created JSON files."""
        for filename in ("Rectangle.json", "Square.json"):
            if os.path.exists(filename):
                os.remove(filename)

    def test_save_rectangle_list(self):
        """Test saving a list of Rectangles creates the correct file."""
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertIn('"width": 10', content)

    def test_save_none(self):
        """Test saving None creates an empty list file."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertEqual(content, "[]")


class TestCreate(unittest.TestCase):
    """Tests for Base.create."""

    def test_create_rectangle(self):
        """Test creating a Rectangle instance from a dictionary."""
        r1 = Rectangle(3, 5, 1)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

    def test_create_square(self):
        """Test creating a Square instance from a dictionary."""
        s1 = Square(5, 1, 2, 10)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)


class TestLoadFromFile(unittest.TestCase):
    """Tests for Base.load_from_file."""

    def tearDown(self):
        """Clean up any created JSON files."""
        for filename in ("Rectangle.json", "Square.json"):
            if os.path.exists(filename):
                os.remove(filename)

    def test_load_no_file_returns_empty_list(self):
        """Test loading when no file exists returns an empty list."""
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_save_and_load_rectangles(self):
        """Test saving and then loading a list of Rectangles."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 2)
        self.assertEqual(str(loaded[0]), str(r1))
        self.assertEqual(str(loaded[1]), str(r2))


if __name__ == "__main__":
    unittest.main()
