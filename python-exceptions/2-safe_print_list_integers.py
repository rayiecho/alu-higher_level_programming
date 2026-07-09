#!/usr/bin/python3
"""Module that prints the first x integers of a list."""


def safe_print_list_integers(my_list=[], x=0):
    """Print the integers among the first x elements of my_list."""
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print()
    return count
