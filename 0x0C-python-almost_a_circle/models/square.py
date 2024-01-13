#!/usr/bin/python3
"""
This module contains a Square class, which inherits from the Rectangle class.
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Represents a square, inheriting from the Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a square.

        Parameters:
        - size (int): Side length of the square.
        - x (int): X-coordinate of the square.
        - y (int): Y-coordinate of the square.
        - id (int): Unique identifier for the square.
        """
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Defines a format for the string representation of the class.

        Returns:
        - str: String representation of the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """
        Gets the value of the size attribute.

        Returns:
        - int: Size of the square.
        """
        return self.__width

    @size.setter
    def size(self, value):
        """
        Sets the value for the size attribute.

        Parameters:
        - value (int): New size value.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """
        Updates attributes of an instance.

        Parameters:
        - args (tuple): Variable length argument list.
        - kwargs (dict): Arbitrary keyword arguments.
        """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Square.

        Returns:
        - dict: Dictionary representation of the square.
        """
        obj_dictionary = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return obj_dictionary
