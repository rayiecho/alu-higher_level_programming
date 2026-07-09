#!/usr/bin/python3
"""Module that prints all integers of a list, in reverse order."""


def print_reversed_list_integer(my_list=[]):
    """Print every integer in my_list, one per line, in reverse order."""
    if my_list is None:
        return
    for i in reversed(my_list):
        print("{:d}".format(i))
