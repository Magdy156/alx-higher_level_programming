#!/usr/bin/python3
"""Define a rectangle class"""


class Rectangle:
    """represent a rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """rectangle constructor
        Args:
            width (int): the width of the rec
            height (int): the height of the rec
        """
        Rectangle.number_of_instances += 1
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
        if self.__width == 0 or self.height == 0:
            return (0)
        return (2 * self.__width + 2 * self.__height)

    def __str__(self):
        """Return the rect in # form
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = []
        for i in range(self.__height):
            for j in range(self.__width):
                rect.append(str(Rectangle.print_symbol))
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """return the string representation of rec"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """print a message at th deletion of a rect"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
