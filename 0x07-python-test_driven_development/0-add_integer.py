#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """function that adds 2 integers.
    Raises:
        TypeError: if a or b not int or float
    Returns:
        the integer addition of a and b
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
