#!/usr/bin/python3
"""Module that replaces all occurrences of an element in a new list."""


def search_replace(my_list, search, replace):
    """Return a new list with search replaced by replace."""
    new_list = my_list[:]
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
    return new_list
