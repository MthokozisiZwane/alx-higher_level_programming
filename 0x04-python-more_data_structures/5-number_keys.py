#!/usr/bin/python3
def number_keys(a_dictionary):
    number = 0
    keys = list(a_dictionary.keys())

    for i in keys:
        number += 1

    return (number)
