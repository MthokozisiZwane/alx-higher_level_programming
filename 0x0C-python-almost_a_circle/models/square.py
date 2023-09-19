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

    def __str__(self):
        """
        Returns a string representation of the Square instance.

        Returns:
            str: A string representing the Square instance.
        """
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)
