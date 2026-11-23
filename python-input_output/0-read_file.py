#!/usr/bin/python3
"""Reads a text file (UTF-8) and prints its content to stdout."""


def read_file(filename=""):
    """Print the contents of a UTF-8 text file to stdout."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
