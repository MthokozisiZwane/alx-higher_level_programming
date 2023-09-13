#!/usr/bin/python3
"""
8-class_to_json
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data \
            structure (list, dictionary, string, integer, and boolean)
    for JSON serialization of an object.
    Args:
        obj: The object to be converted to a dictionary.

    Returns:
        dict: The dictionary representation of the object.
    """
    return obj.__dict__
