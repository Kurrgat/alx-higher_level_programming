#!/usr/bin/python3
"""
Checks if an object is an instance of, or inherited from, a specified class
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or inherited from,
    the specified class; otherwise, False.

    Args:
        obj: Object to check.
        a_class: Class to compare against.
    """
    return isinstance(obj, a_class)
