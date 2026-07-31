#!/usr/bin/python3
"""Defines the Square class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square, inheriting from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the square (width and height).
            x (int): The x coordinate of the square.
            y (int): The y coordinate of the square.
            id (int): The identity of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the square (maps to width and height)."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return the printable representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update attributes via no-keyword or keyword arguments.

        Args:
            *args: New attribute values in order: id, size, x, y.
            **kwargs: New attribute values by name.
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }
