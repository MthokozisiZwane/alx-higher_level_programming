#!/usr/bin/python3
"""Returns true if object is an instance of specified  class"""


def is_same_class(obj, a_class):
    """Returns True if obj is an instance of specified class, else False."""
    return type(obj) == a_class
