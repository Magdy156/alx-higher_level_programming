#!/usr/bin/python3
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """append a string to a UTF8 text file.
    Args:
        filename (str): file name
        text (str): text to be written
    Returns:
        The number of characters written.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
