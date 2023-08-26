#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())

    for value_key in list_keys:
        if value == a_dictionary.get(value_key):
            del a_dictionary[value_key]

    return (a_dictionary)
