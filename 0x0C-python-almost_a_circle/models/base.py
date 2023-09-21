#!/usr/bin/python3


"""
The base class for all classes in this project
"""
import json
import csv


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

    @staticmethod
    def from_json_string(json_string):
        """
         returns the list of the JSON string representation json_string
         """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):

        """
        this method returns an instance with all attributes already set:

        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            return None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        It loads JSON data from a file and creates instances.
        It returns a list of instances
        The filename must be: <Class name>.json - \
                example: Rectangle.json
        If the file doesn’t exist, return an empty list
        Otherwise, return a list of instances - the type of these \
                instances depends on cls (current class using this method)
        You must use the from_json_string and \
                create methods (implemented previously)
        """
        file_name = cls.__name__ + ".json"
        instances = []

        try:
            with open(file_name, "r") as file:
                json_data = file.read()
                if json_data:
                    json_list = cls.from_json_string(json_data)
                    instances = [cls.create(**data) for data in json_list]
        except FileNotFoundError:
            pass
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """The method Serialize list_objs to CSV file"""
        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            if cls.__name__ == 'Rectangle':
                for obj in list_objs:
                    writer.writerow
                    ([obj.id, obj.width, obj.height, obj.x, obj.y])
            elif cls.__name__ == 'Square':
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """This method Deserializes objects from CSV file"""
        filename = cls.__name__ + ".csv"
        obj_list = []
        try:
            with open(filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                if cls.__name__ == 'Rectangle':
                    for row in reader:
                        obj = cls.create(id=int(row[0]))
                        obj.update(int(row[1]),
                                   int(row[2]), int(row[3]), int(row[4]))
                        obj_list.append(obj)
                elif cls.__name__ == 'Square':
                    for row in reader:
                        obj = cls.create(id=int(row[0]))
                        obj.update(int(row[1]), x=int(row[2]), y=int(row[3]))
                        obj_list.append(obj)
        except FileNotFoundError:
            pass
        return obj_list
