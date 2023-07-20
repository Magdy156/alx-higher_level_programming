#!/usr/bin/python3
"""Defines a base model class"""


class Base:
    """Represts a base for other classes in this project
    Private Class Attributes:
        __nb_object (int): Number of instants from the base."""

    __nb_objects = 0

    def __init__(self, id=None):
        if (id):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects