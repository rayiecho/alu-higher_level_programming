#!/usr/bin/python3
"""Module that safely divides two integers."""


def safe_print_division(a, b):
    """Divide a by b, print the result, and return it (None on error)."""
    result = None
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(result))
