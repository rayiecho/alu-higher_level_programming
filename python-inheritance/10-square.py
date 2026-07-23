#!/usr/bin/python3
"""Defines a Square class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, inheriting from Rectangle."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
