#!/usr/bin/python3
"""
Created on Sat Sep  2 12:02:13 2023

@author: mthokozisi zwane
"""


def add_integer(a, b=98):
    """
     This function Adds two integers.
    """
    if not (isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    if not (isinstance(b, (int, float))):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
