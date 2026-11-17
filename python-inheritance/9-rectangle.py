#!/usr/bin/python3
"""This module defines a full Rectangle class based on BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle with a private, validated width and height."""

    def __init__(self, width, height):
        """Initialize a new Rectangle with a width and a height."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description as [Rectangle] width/height."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
