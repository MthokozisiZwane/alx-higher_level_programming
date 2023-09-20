#!/usr/bin/python3

"""
Created on Mon Sep 18 13:12:30 2023

@author: mtho
"""
from models.rectangle import Rectangle
# from rectangle8 import Rectangle  # for working in spyder


class Square(Rectangle):
    """
    A square class that inherits from Rectangle.

    Attributes:
        size (int): The size of the square.
        x (int): The x-coordinate of the square's position.
        y (int): The y-coordinate of the square's position.
        id (int): The unique identifier for the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square's position \
                    (default is 0).
            y (int, optional): The y-coordinate of the square's position \
                    (default is 0).
            id (int, optional): The unique identifier for the square \
                    (default is None).
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size value.

        Note:
            This setter method also updates the width and height \
                    to maintain the square's dimensions.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Square instance.

        This method allows you to update the attributes of the Square \
                instance using either positional \
                arguments or keyword arguments.

        Args:
            *args: Variable number of positional arguments. \
                    The first argument updates the 'id' attribute, the \
                    second updates 'size', the third updates 'x', \
                    and the fourth updates 'y', if provided.

            **kwargs: Arbitrary keyword arguments. \
                    You can specify attribute-value pairs as keyword \
                    arguments to update specific attributes. \
                    Valid attribute names are 'id', 'size', 'x', and 'y'.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def __str__(self):
        """
        Returns a string representation of the Square instance.

        Returns:
            str: A string representing the Square instance.
        """
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        """
        Return the dictionary representation of the square instance

        Returns:
            dict: A dictionary containing attributes of the square \
                    instance  including 'id,' 'width,' 'x,' and 'y.'
        """
        return {
                'id': self.id,
                'width': self.width,
                'x': self.x,
                'y': self.y
                }
