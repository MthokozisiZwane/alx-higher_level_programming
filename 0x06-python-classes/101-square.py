#!/usr/bin/python3
""" A Class that defines a square"""


class Square:
    """
    A class representing a square.

    Attributes:
        size (int): The size of the square's sides.
        position (tuple): The position of the square's top-left corner.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance.

        Args:
            size (int, optional): The size of the square's sides.
            position (tuple, optional):
                The position of the square's top-left corner.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square's sides.

        Returns:
            int: The size of the square's sides.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square's sides.

        Args:
            value (int): The size value to be set.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square's top-left corner.

        Returns:
            tuple: The position of the square's top-left corner.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square's top-left corner.

        Args:
            value (tuple): The position value to be set.

        Raises:
            TypeError: If the provided value is
                not a tuple of 2 positive integers.
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(i, int) for i in value)
            or not all(i >= 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the character '#' to stdout.

        If the size is 0, an empty line is printed.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
