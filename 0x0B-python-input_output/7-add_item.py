#!/usr/bin/python3
"""
7-add_item
"""


import json
import sys


def load_add_save():
    """
    Loads a list from a JSON file, adds the command line \
            arguments to the list, and saves it back to the file.
    """
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])

    save_to_json_file(items, "add_item.json")


if __name__ == "__main__":
    load_add_save()
