#!/usr/bin/python3


"""
The base class for all classes in this project
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the json string representation of list_dictionaries
        """
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
