#!/usr/bin/python3
"""
This module contains a function to find a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.
    """
    if not list_of_integers:
        return None
    low, high = 0, len(list_of_integers) - 1

    while low < high:
        midd = (low + high) // 2
        if list_of_integers[midd] > list_of_integers[midd + 1]:
            high = midd
        else:
            low = midd + 1

    return list_of_integers[low]
