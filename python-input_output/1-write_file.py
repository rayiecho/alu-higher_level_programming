#!/usr/bin/python3
"""Defines a write_file function."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file, overwriting existing content.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
