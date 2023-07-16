#!/usr/bin/python3
"""Define an empty class"""


class BaseGeometry:
    """Represent base geometery"""
    def area(self):
        """will not be implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the value
        Args:
            name (str): the param name
            value (int): value to be validated
        Raises:
            TypeError: if not int
            ValueError: if <= zero
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{}  must be greater than 0".format(name))
