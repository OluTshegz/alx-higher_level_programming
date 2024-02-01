#!/usr/bin/python3
"""Task 3. Print square: This module
    has one function that prints a
    square with the character '#'."""


def print_square(size):
    """ prints a square with the character '#'
    Args:
        size (int): the size length of the square
    Raises:
        TypeError: if size is not an integer
        TypeError: if size is a float and is less than 0
        ValueError: if size is less than 0"""

    if (type(size) is not int):
        raise TypeError("size must be an integer")

    if (size < 0):
        raise ValueError("size must be >= 0")

    if (type(size) is float and size < 0):
        raise("size must be an integer")

    for row in range(size):
        for elem in range(size):
            print("#", end="")
        print()
