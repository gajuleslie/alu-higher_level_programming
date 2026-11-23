#!/usr/bin/python3
"""Defines a Student class that can be serialized and reloaded."""


class Student:
    """Represents a student with a first name, last name and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student.

        If attrs is a list of strings, only the named attributes are returned.
        Otherwise, all attributes are returned.
        """
        if (attrs is None or not isinstance(attrs, list) or
                not all(isinstance(attr, str) for attr in attrs)):
            return self.__dict__
        return {key: value for key, value in self.__dict__.items()
                if key in attrs}

    def reload_from_json(self, json):
        """Replace the Student's attributes with the values in json."""
        for key, value in json.items():
            setattr(self, key, value)
