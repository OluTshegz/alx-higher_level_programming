#!/usr/bin/python3
"""Task 1. Divide a matrix: This module has one
    function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """returns the division of all elements of a matrix
    Args:
        matrix: A list of lists - members can be of type ints or floats
        div: Number to be used for the division (can be a float or an integer)
    Raises:
        TypeError: If the matrix contains non-numbers
        TypeError: If the matrix contains rows of different sizes
        TypeError: If div is not an int or float
        ZeroDivisionError: If div is 0
    Returns:
        A new matrix which represents the result of the divisions"""

    if (matrix is None or (type(matrix) is not list) or
        any(type(row) is not list for row in matrix) or
        any(type(elem) not in [int, float]
            for row in matrix for elem in row)):
        raise TypeError("matrix must be a matrix (list "
                        "of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if (type(div) not in [int, float]):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = []

    for row in matrix:
        rounded_row = []
        for x in row:
            rounded_value = round(x / div, 2)
            rounded_row.append(rounded_value)
        result.append(rounded_row)

    return result
