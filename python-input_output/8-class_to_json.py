#!/usr/bin/python3
"""Returns the dictionary description for JSON serialization of an object."""


def class_to_json(obj):
    """Return the instance attributes of obj as a dictionary."""
    return obj.__dict__
