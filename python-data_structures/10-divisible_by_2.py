#!/usr/bin/python3
"""Module that finds all multiples of 2 in a list."""


def divisible_by_2(my_list=[]):
    """Return a list of booleans indicating multiples of 2."""
    result = []
    for i in my_list:
        result.append(i % 2 == 0)
    return result
