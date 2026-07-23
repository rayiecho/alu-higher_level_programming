#!/usr/bin/python3
"""Defines a BaseGeometry class."""


class BaseGeometry:
    """Represents a base for geometry classes."""

    def area(self):
        """Raise an exception since area() is not implemented."""
        raise Exception("area() is not implemented")
