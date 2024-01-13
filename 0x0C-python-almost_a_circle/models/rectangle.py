#!/usr/bin/python3
"""
module containing the Rectangle class.
"""

from models.base import Base

class Rectangle(Base):
    """
    Represents a rectangle object, inheriting from the Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes attributes of the rectangle.

        Parameters:
        - width (int): Width of the rectangle.
        - height (int): Height of the rectangle.
        - x (int): X-coordinate of the rectangle.
        - y (int): Y-coordinate of the rectangle.
        - id (int): Unique identifier for the rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # List of getter functions
    @property
    def width(self):
        """
        Getter for the width attribute.

        Returns:
        - int: Width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """
        Getter for the height attribute.

        Returns:
        - int: Height of the rectangle.
        """
        return self.__height

    @property
    def x(self):
        """
        Getter for the x attribute.

        Returns:
        - int: X-coordinate of the rectangle.
        """
        return self.__x

    @property
    def y(self):
        """
        Getter for the y attribute.

        Returns:
        - int: Y-coordinate of the rectangle.
        """
        return self.__y

    # List of setter functions
    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.

        Parameters:
        - value (int): New width value.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.

        Parameters:
        - value (int): New height value.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """
        Setter for the x attribute.

        Parameters:
        - value (int): New x-coordinate value.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """
        Setter for the y attribute.

        Parameters:
        - value (int): New y-coordinate value.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
        - int: Area of the rectangle.
        """
        return (self.__height * self.__width)

    def display(self):
        """
        Displays the rectangle using '#' characters.
        """
        for _ in range(self.y):
            print()
        for _ in range(self.__height):
            print(" " * self.x + "#" * self.__width)

    def __str__(self):
        """
        Returns a string representation of the rectangle object.

        Returns:
        - str: String representation of the rectangle.
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the rectangle.

        Parameters:
        - args (tuple): Variable length argument list.
        - kwargs (dict): Arbitrary keyword arguments.
        """
        # ...

    def to_dictionary(self):
        """
        Returns a dictionary representation of the rectangle.

        Returns:
        - dict: Dictionary representation of the rectangle.
        """
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }
