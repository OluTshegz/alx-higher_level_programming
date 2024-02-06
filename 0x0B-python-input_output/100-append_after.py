#!/usr/bin/python3
"""This module defines a text file-insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file,
    after each line containing a specific string
    Args:
        filename (str): The name of the file to change/modify.
        search_string (str): The string to search for within the file.
        new_string (str): The new string to add/insert.
    """
    text = ""
    with open(filename, 'r', encoding="utf-8") as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w", encoding="utf-8") as w:
        w.write(text)
