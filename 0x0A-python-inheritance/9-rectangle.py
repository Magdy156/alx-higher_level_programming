#!/usr/bin/python3
"""Defines a class  that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle"""
    def __init__(self, width, height):
        """Intialize a new rectangle
        Args:
            width (int): rect width
            height (int): rect height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """return the rect area"""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of the rect"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
