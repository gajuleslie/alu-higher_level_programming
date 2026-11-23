#!/usr/bin/python3
"""Appends a string to a UTF-8 text file."""


def append_write(filename="", text=""):
    """Append text to filename and return the number of characters added."""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
