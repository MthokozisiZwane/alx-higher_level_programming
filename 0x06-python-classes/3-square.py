#!/usr/bin/python3
"""Defines a square class."""


class Square:
    """A class that defines/represents a square."""
    def __init__(self, size=0):
        """Initializes a new square instance.

        Args:
            size (int): The size of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
