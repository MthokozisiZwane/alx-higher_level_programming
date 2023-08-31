#!/usr/bin/python3
"""Defines a square class."""


class Square:
    """A class that defines a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new square instance.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.
        Raises:
            TypeError: If size is not an integer or position
                is not a tuple of 2 positive integers.
            ValueError: If size is less than 0
                or position coordinates are not positive.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(coordin, int) and
                   coord >= 0 for coordin in position):
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    @property
    def size(self):
        """Gets or sets the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The new size value.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets or set the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square.

        Args:
            value (tuple): The new position value.
        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
            ValueError: If position coordinates are not positive.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(coordin, int) and
                   coordin >= 0 for coordin in value):
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints the square using '#' characters and position."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
