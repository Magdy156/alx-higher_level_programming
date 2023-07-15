#!/usr/bin/python3
"""Defines a class inherits from list"""


class MyList(list):
    """ inherits from list"""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print(sorted(self))
