#!/usr/bin/python3
"""Divide a matrix.

This module provides a function that divides every element of a matrix
by a number and returns a new matrix rounded to two decimal places.

"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Returns a new matrix whose elements are rounded to two decimals.
    """
    if (not isinstance(matrix, list) or not matrix or
            not all(isinstance(row, list) for row in matrix) or
            not all(type(item) in (int, float)
                    for row in matrix for item in row)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in row] for row in matrix]
