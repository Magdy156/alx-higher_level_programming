#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return (None)
    keys = list(a_dictionary.keys())
    maxVal = a_dictionary[keys[0]]
    maxKey = keys[0]
    for key in keys:
        if a_dictionary[key] > maxVal:
            maxVal = a_dictionary[key]
            maxKey = key
    return (maxKey)
