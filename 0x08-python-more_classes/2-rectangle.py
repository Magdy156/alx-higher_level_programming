#!/usr/bin/python3
"""Define a rectangle class"""


class Rectangle:
    """represent a rectangle"""
    def __init__(self, width=0, height=0):
        """rectangle constructor
        Args:
            width (int): the width of the rec
            height (int): the height of the rec
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter and setter"""
        return self.__width

    @width.setter
    def width(self, newVal):
        if not isinstance(newVal, int):
            raise TypeError('width must be an integer')
        if newVal < 0:
            raise ValueError('width must be >= 0')
        self.__width = newVal

    @property
    def height(self):
        """height getter and setter"""
        return self.__height

    @height.setter
    def height(self, newVal):
        if not isinstance(newVal, int):
            raise TypeError('height must be an integer')
        if newVal < 0:
            raise ValueError('height must be >= 0')
        self.__height = newVal

    def area(self):
        """return the rec area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """return the rec perimeter"""
        return (2 * self.__width + 2 * self.__height)
