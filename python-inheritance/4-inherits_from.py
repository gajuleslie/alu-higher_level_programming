#!/usr/bin/python3
"""This module defines a function that checks inherited classes."""


def inherits_from(obj, a_class):
    """Return True if obj's class inherited from a_class, directly or not.

    The object must not be an exact instance of a_class itself.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
