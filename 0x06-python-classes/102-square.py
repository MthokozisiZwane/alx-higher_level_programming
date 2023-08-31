#!/usr/bin/python3
""" A class that defines a square"""


class Square:
    """
    A class representing a square.

    Attributes:
        size (float or int): The size of the square's sides.
    """
    def __init__(self, size=0):
        """
        Initialize a Square instance.

        Args:
            size (float or int, optional): The size of the square's sides.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieve the size of the square's sides.

        Returns:
            float or int: The size of the square's sides.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """s
        Set the size of the square's sides.

        Args:
            value (float or int): The size value to be set.

        Raises:
            TypeError: If the provided value
                is not a number (float or integer).
            ValueError: If the provided value is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Compares if two squares are equal based on their areas.

        Args:
            other (Square): Another Square object to compare.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Compares if two squares are not equal based on their areas.

        Args:
            other (Square): Another Square object to compare.

        Returns:
            bool: True if the areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Compares if the area of one square is less
            than the area of another square.

        Args:
            other (Square): Another Square object to compare.

        Returns:
            bool: True if the area of the current square
                is less, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Compares if the area of one square is less
            than or equal to the area of another square.

        Args:
            other (Square): Another Square object to compare.

        Returns:
            bool: True if the area of the current
                square is less than or equal, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Compares if the area of one square
            is greater than the area of another square.

        Args:
            other (Square): Another Square object to compare.

        Returns:
            bool: True if the area of the current
                square is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Compares if the area of one square is greater
            than or equal to the area of another square.

        Args:
            other (Square): Another Square object to compare.

        Returns:
            bool: True if the area of the current square is
                greater is greater than or equal, False otherwise.
        """
        return self.area() >= other.area()
