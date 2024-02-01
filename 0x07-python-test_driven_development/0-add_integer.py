#!/usr/bin/python3
"""Task 0. Integers addition:
    This module has one function that adds 2 integers."""


def add_integer(a, b=98):
    """returns the sum of two integers or floats as integers
    Args:
        a (int/ float): first argument to be added
        b (int/ float): second argument to be added with default value 98
    Raises:
        TypeError: If either of the arguments not an integer or a float
    Returns:
        Sum of the two arguments"""

    if a is None or (type(a) not in [int, float]):
        """a must be an int or float else raise TypeError"""
        raise TypeError("a must be an integer")
    if b is None or (type(b) not in [int, float]):
        """b must be an int or float else raise TypeError"""
        raise TypeError("b must be an integer")
    return int(a) + int(b)
