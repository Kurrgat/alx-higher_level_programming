#!/usr/bin/python3
"""
Defines a function that checks if an object is exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class; otherwise, False.

    Args:
        obj: Object to check.
        a_class: Class to compare against
    """
    return type(obj) is a_class
