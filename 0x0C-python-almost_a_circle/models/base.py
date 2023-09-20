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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a list of objects to JSON file
        This class method takes a list of objects and serializes\
                them to a JSON file with the name of the class
        appended with '.json'. It converts each object into a dictionary\
            representation using the 'to_dictionary'
        method of the objects and then writes the list o\
            f dictionaries to the JSON file.
        """

        filename = cls.__name__ + ".json"
        json_list = []

        if list_objs is not None:
            for obj in list_objs:
                json_list.append(obj.to_dictionary())

        with open(filename, "w") as file:
            file.write(cls.to_json_string(json_list))
