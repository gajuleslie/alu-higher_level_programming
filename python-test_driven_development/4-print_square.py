#!/usr/bin/python3
"""Print a square.

This module provides a function that prints a square made of hash
characters with the given size.

"""


def print_square(size):
    """Print a square of hash characters.

    Prints size rows of size hash characters when size is positive.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
