#!/usr/bin/python3


"""
The base class for all classes in this project
"""


class Base:
    """
    private class attribute
    """
    __nb_objects = 0

    """initializes instance"""

    def __init__(self, id=None):

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
