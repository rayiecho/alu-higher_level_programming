#!/usr/bin/python3
"""Module that replaces an element in a list without modifying original."""


def new_in_list(my_list, idx, element):
    """Return a copy of my_list with idx replaced by element."""
    new_list = my_list[:]
    if idx < 0 or idx >= len(new_list):
        return new_list
    new_list[idx] = element
    return new_list
