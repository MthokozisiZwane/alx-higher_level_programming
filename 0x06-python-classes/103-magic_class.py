#!/usr/bin/python3
""" A class that does the same as the given bytecode"""

import math


class MagicClass:
    """
    A class that mimics the behavior of the given bytecode.
    """
    def __init__(self, radius=0):
        """
        Initializes a MagicClass instance.

        Args:
            radius (float or int, optional): The radius value. Defaults to 0.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius


if __name__ == "__main__":
    magic = MagicClass(3)
    print("Area:", magic.area())
    print("Circumference:", magic.circumference())
