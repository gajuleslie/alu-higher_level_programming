#!/usr/bin/python3
"""Returns Pascal's triangle of a given size."""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's triangle of n rows."""
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        previous = triangle[i - 1]
        row = [1]
        for j in range(1, i):
            row.append(previous[j - 1] + previous[j])
        row.append(1)
        triangle.append(row)
    return triangle
