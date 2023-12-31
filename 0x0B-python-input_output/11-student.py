#!/usr/bin/python3
"""
11-student
"""


class Student:
    """
    Class Student defining a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.
        Returns:
            dict: The dictionary representation of the student.
        """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }

    def reload_from_json(self, json_data):
        self.first_name = json_data['first_name']
        self.last_name = json_data['last_name']
        self.age = json_data['age']
