#!/usr/bin/python3


"""
Created on Sat Sep  2 20:59:25 2023

@author: Mtho
"""


def print_square(size):
    """
    Prints a square with the character #

    Args:
    ----------
    size(int) : The length of the square


    Returns:
        A square

    Raises:
        TypeError: If size is not an integer,and\
                   if size is a float and less than 0
        ValueError: if size is less than zero

    Examples:
        >>> print_square(4)
        >>> ####
            ####
            ####
            ####

    """

    if not(isinstance(size, int)):
        raise TypeError("size must be an integer")
    if(isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):

        print(size * "#")
