#!/usr/bin/python3
"""
Module containing a class Square that defines a square.
"""


class Square:
    """
    Class Square with a private instance attribute size.
    """
    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Parameters:
            - size (int): The size of the square.
        """
        self.__size = size
