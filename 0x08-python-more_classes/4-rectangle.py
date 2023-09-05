#!/usr/bin/python3
""" A class defining a rectangle"""


class Rectangle:
    """ A class representing a rectangle"""
    def __init__(self, width=0, height=0):
        """ Initializes a new rectangle instance.

        Args:
        width(int): the width of the rectangle
        height(int): the height of the rectangle
        Raises:
        TypeError: if height or width is not an integer
        ValueError: if width or height is less than zero
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ Gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Sets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the height of rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Calculates the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """ Calculates the perimeter of rectangle"""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ returns rectangle as a string of # chars"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(['#' * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Returns a string representation of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"
