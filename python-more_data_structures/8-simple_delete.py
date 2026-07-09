#!/usr/bin/python3
"""Module that deletes a key in a dictionary."""


def simple_delete(a_dictionary, key=""):
    """Delete key from a_dictionary if present, return a_dictionary."""
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
