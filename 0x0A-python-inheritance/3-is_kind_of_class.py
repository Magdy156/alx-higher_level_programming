#!/usr/bin/python3
"""Defines a class and inherited class-checking function"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.
    Args:
        obj (any): The object to be check.
        a_class (type): The class to be compared
    Returns:
        True or False
    """
    if isinstance(obj, a_class):
        return True
    return False
