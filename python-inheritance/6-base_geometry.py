#!/usr/bin/python3
"""This module defines a BaseGeometry class with an area method."""


class BaseGeometry:
    """Represents the base class for all geometry shapes."""

    def area(self):
        """Raise an Exception because the area is not implemented here."""
        raise Exception("area() is not implemented")
