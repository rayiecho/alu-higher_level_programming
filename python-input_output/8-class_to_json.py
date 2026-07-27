#!/usr/bin/python3
"""Defines a class_to_json function."""


def class_to_json(obj):
    """Return the dictionary description of a simple data-structure object.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: The dictionary representation of obj.
    """
    return obj.__dict__
