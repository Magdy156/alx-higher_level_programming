#!/usr/bin/python3
# 4-inherits_from.py
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class
    Args:
        obj (any): The object to be checked
        a_class (type): class to be compared
    Returns:
        True or False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
