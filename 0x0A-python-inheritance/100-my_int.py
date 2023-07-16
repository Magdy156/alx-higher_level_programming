#!/usr/bin/python3
"""Defines a class inherits from int"""


class MyInt(int):
    """Invert int operators == and !="""
    def __init__(self, value):
        """Initialise value"""
        self.__invert = value

    def __eq__(self, value):
        """Override == opeartor with != behavior"""
        return self.__invert != value

    def __ne__(self, value):
        """Override != operator with == behavior"""
        return self.__invert == value
