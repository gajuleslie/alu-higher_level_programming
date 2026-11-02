#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    return [[value ** 2 for value in row] for row in matrix]
