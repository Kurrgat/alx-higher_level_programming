#!/usr/bin/python3
"""
Defines a class BaseGeometry with a public instance method area()
that raises an Exceptionwith the message 'area() is not implemented'.
"""


class BaseGeometry:
    """
    Defines a base geometry class.
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")
