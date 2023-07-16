#!/usr/bin/python3
"""Defines a function  adds attributes to objects"""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible
    Args:
        obj (any): The object to add an attribute to
        att (str): Attribute to be added
        value (any): Attribute value
    Raises:
        TypeError: If the attribute can not be added
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
