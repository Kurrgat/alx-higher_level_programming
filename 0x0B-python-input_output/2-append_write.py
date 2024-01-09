#!/usr/bin/python3
"""
This module appends a string to the end of a text file (UTF8)
and returns the number of characters added.
"""


def append_write(filename="", text=""):
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
