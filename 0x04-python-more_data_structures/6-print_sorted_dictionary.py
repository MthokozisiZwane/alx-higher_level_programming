#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ordered = list(a_dictionary.keys())
    ordered.sort()
    for i in ordered:
        print("{}: {}".format(i, a_dictionary.get(i)))
