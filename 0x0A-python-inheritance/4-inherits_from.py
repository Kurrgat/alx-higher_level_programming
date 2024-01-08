#!/usr/bin/python3
"""
checks if the object is an instance of a class that inherited
(directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise, False.

    Args:
        obj: Object to check.
        a_class: Class to compare against.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
