#!/usr/bin/python3
"""Indent text.

This module provides a function that prints text with two new lines
after each period, question mark, or colon.

"""


def text_indentation(text):
    """Print text with two new lines after '.', '?', and ':'.

    Leading spaces after a new line or delimiter are skipped.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == " ":
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == " ":
                c += 1
            continue
        c += 1
