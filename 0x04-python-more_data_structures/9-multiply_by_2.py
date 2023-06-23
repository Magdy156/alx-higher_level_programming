#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    copy = a_dictionary.copy()
    keys = list(copy.keys())
    for key in keys:
        copy[key] *= 2
    return (copy)
