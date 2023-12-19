#!/usr/bin/python3

"""a class Square that defines a square """


class Square:
    """define a Square."""
    
    def __init__(self, size=0):
        """Create a Square
        Args: size: length of side of a Square
        """
        
        if not isinstance(size, (int, float)):
            raise TypeError("size must be a number")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        """"The property of size as the len of a side of Square
        Raises:
            TypeError: if size != int
            ValueErrorr: if size < 0
        """
        
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        return self.__size * self.__size

    def __eq__(self, other):
        if isinstance(other, Square):
            return self.area() == other.area()

        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, Square):
            return self.area() < other.area()

        raise TypeError("Cannot compare Square with non-Square object")

    def __le__(self, other):
        return self.__lt__(other) or self == other

    def __gt__(self, other):
        if isinstance(other, Square):
            return self.area() > other.area()

        raise TypeError("Cannot compare Square with non-Square object")

    def __ge__(self, other):
        return self.__gt__(other) or self == other
