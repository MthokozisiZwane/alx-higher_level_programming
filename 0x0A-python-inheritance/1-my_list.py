#!/usr/bin/python3

class MyList(list):
    """A custom list class that inherits the attributesof built-in list."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
