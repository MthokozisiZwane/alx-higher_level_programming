#!/usr/bin/python3
""" A Class that inherits attributes of list"""


class MyList(list):
    """A custom list class that inherits the attributes of list."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
