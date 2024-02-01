#!/usr/bin/python3
"""Task 4. Text indentation:
    This module has one function
    that prints a text with
    2 new lines after each of these
    characters: '.', '?' and ':'."""


def text_indentation(text):
    """prints a text with
    2 new lines after each of these
    characters: '.', '?' and ':'.
    Args:
        text (str): a string to be printed
    Raises:
        TypeError: if text is not a string"""

    if (type(text) is not str):
        raise TypeError("text must be a string")

    characters = ['.', '?', ':']

    current_line = ''
    for char in text:
        current_line += char
        if char in characters:
            print(current_line.strip())
            print()
            current_line = ''

    if current_line.strip():
        print(current_line.strip())
