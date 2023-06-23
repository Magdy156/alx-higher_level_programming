#!/bin/python3
def update_dictionary(a_dictionary, key, value):
    keys = list(a_dictionary.keys())
    for _key in keys:
        if _key == key:
            a_dictionary[key] = value
    a_dictionary[key] = value
    return (a_dictionary)
