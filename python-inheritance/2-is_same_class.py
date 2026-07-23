#!/usr/bin/python3
"""Defines an is_same_class function."""


def is_same_class(obj, a_class):
    """Check if obj is exactly an instance of a_class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        bool: True if obj's type is exactly a_class, else False.
    """
    return type(obj) is a_class
