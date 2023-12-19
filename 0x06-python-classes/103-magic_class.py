#!/usr/bin/python3

"""class MagicClass """


class MagicClass:
    """set up magic class"""
    
    def __init__(self, radius):
        """ write docstring """

        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')

        self._MagicClass__radius = radius

    def area(self):
        """again with docstring"""
        
        return self._MagicClass__radius**2 * math.pi

    def circumference(self):
        """another docstring"""
        
        return 2 * math.pi * self._MagicClass__radius
