#!/usr/bin/python3
""" A class of base geometry"""


class BaseGeometry:
    """A class representing base geometry."""

    def area(self):
        """Raises an Exception with message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the 'value' parameter:
        - 'name' must be a string
        - 'value' must be an integer
        - 'value' must be greater than 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
