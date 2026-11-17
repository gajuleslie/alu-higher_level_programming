#!/usr/bin/python3
"""This module defines a MyList class that inherits from list."""


class MyList(list):
    """Represents a list that can print itself in sorted order."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
