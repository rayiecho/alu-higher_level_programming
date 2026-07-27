#!/usr/bin/python3
"""Defines a save_to_json_file function."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object's JSON representation to a text file.

    Args:
        my_obj: The object to serialize.
        filename (str): The name of the file to write to.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
