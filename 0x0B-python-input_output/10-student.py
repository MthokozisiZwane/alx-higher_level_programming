#!/usr/bin/python3
"""
10-student
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

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student\
                instance with optional attribute filtering.
        Args:
            attrs (list): List of attributes to include\
                    in the dictionary representation.

        Returns:
            dict: The dictionary representation of the student.
        """
        if attrs is None:
            return self.__dict__
        return {attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)}
