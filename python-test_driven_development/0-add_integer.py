#!/usr/bin/python3
"""Add two integers.

This module provides a function that adds two integers or floats after
casting them to integers.

"""


def add_integer(a, b=98):
    """Add two integers.

    Returns the integer sum of a and b after casting floats to integers.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
