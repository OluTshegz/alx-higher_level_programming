#!/usr/bin/python3
"""This module defines a text file-appending_writing funtion"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)
    Args:
        filename (str): The Name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        The number of characters appended"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
