#!/usr/bin/python3
"""Module for printing text with indentation.
"""


def text_indentation(text):
    """Print a text with 2 new lines after each ., ? and : character.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    stripped = text.strip()
    result = ""
    for char in stripped:
        result += char
        if char in ".?:":
            result += "\n\n"

    lines = [line.strip() for line in result.split("\n")]
    print("\n".join(lines), end="")
