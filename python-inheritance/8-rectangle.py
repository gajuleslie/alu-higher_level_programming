#!/usr/bin/python3
"""This module defines a Rectangle class based on BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle with a private, validated width and height."""

    def __init__(self, width, height):
        """Initialize a new Rectangle with a width and a height."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
