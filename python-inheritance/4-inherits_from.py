#!/usr/bin/python3
"""Defines an inherits_from function."""


def inherits_from(obj, a_class):
    """Check if obj is an instance of a class that inherits from a_class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        bool: True if obj's class inherits from a_class (not a_class itself).
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
