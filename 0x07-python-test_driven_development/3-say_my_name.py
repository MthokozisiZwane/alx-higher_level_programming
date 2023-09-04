#!/usr/bin/python3


"""
Created on Sat Sep  2 20:04:04 2023

@author: mtho
"""


def say_my_name(first_name, last_name=""):
    """
    Prints my name is.


    args:
    ----------
    first_name : The first name to print

    last_name : The last name to print


    Returns:
        My name is <first_name> <last_name>
    -------
    Raises:
        TypeError: if first_name and last_name are not strings
    Examples:
        >>> say_my_name("John", "Smith")
        >>> My name is John Smith
        >>>  say_my_name(12, "White")
        >>> first_name must be a string

    """
    if not (isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if not (isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
