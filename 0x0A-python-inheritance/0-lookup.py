#!/usr/bin/python3
"""
    This module returns the list of available attributes
    and methods of an object
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: Object to look up.

    Returns:
        List of attribute and method names.
    """
    return dir(obj)
