#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry"""


class BaseGeometry:
    """
    Defines a base geometry class.
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value:
        - If value is not an integer: raise a TypeError exception 
        with the message '<name> must be an integer'
        - If value is less or equal to 0: raise a ValueError exception
        with the message '<name> must be greater than 0'

        Args:
            name: A string representing the name.
            value: The value to be validated.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
