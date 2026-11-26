#!/usr/bin/python3
"""Say my name.

This module provides a function that prints a formatted full name from
a first name and an optional last name.

"""


def say_my_name(first_name, last_name=""):
    """Print a formatted full name.

    Prints "My name is" followed by the first and last names.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
