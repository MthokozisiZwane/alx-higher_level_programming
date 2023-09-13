#!/usr/bin/python3
"""
0-read_file
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.
    Args:
        filename (str): The name of the file to be read.

    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
