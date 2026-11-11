#!/usr/bin/python3
"""This module defines a Square class with a validated size attribute."""


class Square:
    """Represents a square with a validated size attribute."""

    def __init__(self, size=0):
        """Initialize a new Square with an optional size."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
