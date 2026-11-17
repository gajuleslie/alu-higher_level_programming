#!/usr/bin/python3
"""This module defines a function that checks class membership."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or one of its children."""
    return isinstance(obj, a_class)
