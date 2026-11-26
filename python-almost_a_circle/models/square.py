#!/usr/bin/python3
"""Define the Square class for the Almost a circle project."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square as a rectangle with equal width and height."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance with validated attributes."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Return the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the width and height to the same validated size."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return the formatted string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """Update attributes from positional or keyword arguments."""
        attributes = ["id", "size", "x", "y"]
        if args:
            for attribute, value in zip(attributes, args):
                setattr(self, attribute, value)
        else:
            for attribute, value in kwargs.items():
                if hasattr(self, attribute):
                    setattr(self, attribute, value)

    def to_dictionary(self):
        """Return the dictionary representation of the square."""
        return {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y
        }
