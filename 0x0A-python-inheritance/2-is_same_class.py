#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Check if an object is  an instance of a given class.
    Args:
        obj (any): The object to be checked
        a_class (type): The class will be compared
    Returns:
        true or false
    """
    if type(obj) == a_class:
        return True
    return False
