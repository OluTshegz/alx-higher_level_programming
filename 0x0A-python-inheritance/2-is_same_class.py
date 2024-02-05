#!/usr/bin/python3
"""this module checks if object is an instance of a class"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        bool: If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) is a_class and type(obj) == a_class:
        return True
    return False
