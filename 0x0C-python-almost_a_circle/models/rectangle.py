#!/usr/bin/python3
"""
importing the Base class
"""

from models.base import Base


"""
The rectangle class that inherits fron the Base class
"""


class Rectangle(Base):
    """
    Initializing the variables
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        """ getter and setter methods for width
        """
        @property
        def width(self):
            return self.__width

        """
        The setter method for the width
        """

        @width.setter
        def width(self, value):
            self.__with = value

        """
        Getter and setter method for height
        """

        @property
        def height(self):
            return self.__height

        """
        The setter method for the height
        """

        @height.setter
        def height(self, value):
            self.__height = value

        """
        Getter and setter methods for x
        """
        @property
        def x(self):
            return self.__x

        """
        The setter method for x
        """

        @x.setter
        def x(self, value):
            self.__x = value

        """
        Getter and setter methods for y
        """
        @property
        def y(self):
            return self.__y

        """
        The setter method for y
        """

        @y.setter
        def y(self, value):
            self.__y = value
