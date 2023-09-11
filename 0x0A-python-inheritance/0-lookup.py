#!/usr/bin/python3
""" Function to return attrinutes and methods of an object"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    """
    return dir(obj)
