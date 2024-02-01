#!/usr/bin/python3
"""Task 2. Say my name: This module
    has one function that prints
    'My name is <first name> <last name>'."""


def say_my_name(first_name, last_name=""):
    """prints My name is <first name> <last name>
    Args:
        first_name (str): the first name to be printed
        last_name (str): the last name to be printed
    Raises:
        TypeError: If either first_name or last_name is not string"""

    if (type(first_name) is not str):
        raise TypeError("first_name must be a string")

    if (type(last_name) is not str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
