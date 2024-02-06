#!/usr/bin/python3
"""This module defines a Python class-to-JSON function"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    Args:
        obj (object): The object (a instance of a Class)
        to ready for JSON serialization. All attributes of the obj Class
        are serializable: list, dictionary, string, integer and boolean
    Returns:
        dict: The dictionary description of the object"""
    return obj.__dict__
