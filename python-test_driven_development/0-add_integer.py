#!/usr/bin/python3
"""Module for adding two integers.
"""


def add_integer(a, b=98):
    """Add two integers.

    Args:
        a (int/float): The first number.
        b (int/float): The second number, defaults to 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
