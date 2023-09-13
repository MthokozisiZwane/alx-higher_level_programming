#!/usr/bin/python3
""" 12-pascal_triangle.py

"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle with n rows.
    Args:
        n (int): Number of rows.

    Returns:
        list of lists: Pascal's Triangle as a list of lists.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]

        if triangle:
            last_row = triangle[-1]
            row.extend([last_row[j] + last_row[j + 1]
                       for j in range(len(last_row) - 1)])
            row.append(1)

        triangle.append(row)

    return triangle
