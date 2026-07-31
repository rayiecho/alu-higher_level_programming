#!/usr/bin/python3
"""Module for dividing all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a given divisor.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int/float): The divisor.

    Returns:
        list: A new matrix with all elements divided by div,
            rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of ints/floats,
            if rows aren't all the same size, or if div is not a number.
        ZeroDivisionError: If div is 0.
    """
    err_matrix = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(err_matrix)
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(err_matrix)
        for item in row:
            if type(item) is not int and type(item) is not float:
                raise TypeError(err_matrix)

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(item / div, 2) for item in row] for row in matrix]
