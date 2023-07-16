#!/usr/bin/python3
"""Defines a function reads files"""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout"""
    with open(filename, 'r') as f:
        f.read()
