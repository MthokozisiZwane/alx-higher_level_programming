#!/usr/bin/python3
"""class Square that inherits from Rectangle"""


class BaseGeometry:
    """A class representing base geometry."""

    def area(self):
        """Raises an Exception with message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the 'value' parameter:
        - 'name' must be a string
        - 'value' must be an integer
        - 'value' must be greater than 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """A class representing a rectangle."""

    def __init__(self, width, height):
        """Initializes a rectangle with width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """A class representing a square."""

    def __init__(self, size):
        """Initializes a square with the given size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
