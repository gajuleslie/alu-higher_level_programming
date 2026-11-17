#!/usr/bin/python3
"""This module defines a Square class with its own string description."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square with a private, validated size."""

    def __init__(self, size):
        """Initialize a new Square with a size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Return the square description as [Square] width/height."""
        return "[Square] {}/{}".format(self.__size, self.__size)
