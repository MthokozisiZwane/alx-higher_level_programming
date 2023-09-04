#!/usr/bin/python3


# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 14:51:26 2023

@author: mthokozisi zwane
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given number.

    Args:
        matrix (list of lists): The input matrix,
            where each element is an integer or float.
        div (int or float): The number to divide all elements of the matrix by.

    Returns:
        list of lists: A new matrix where all elements have been divided
            by 'div' and rounded to 2 decimal places.

    Raises:
        TypeError: If 'matrix' is not a list of lists of integers/floats,
            if each row of 'matrix' doesn't have the same size,
                or if 'div' is not a number (integer or float).
        ZeroDivisionError: If 'div' is equal to 0.

    Examples:
        >>> matrix = [[1, 2, 3], [4, 5, 6]]
        >>> matrix_divided(matrix, 3)
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    """
    if not matrix:
        return []
    if not all(isinstance(row, list) and all(isinstance(element, (int, float))
               for element in row) for row in matrix):
        raise TypeError("matrix must be a matrix(list of lists)\
                        of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number (integer or float)")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = [[round(element / div, 2) for element in row] for row in matrix]
    return result
