#!/usr/bin/python3
"""This module defines a class Student"""


class Student:
    """represents the Student class"""
    def __init__(self, first_name, last_name, age):
        """initializes a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """gets/retrieves a dictionary representation of
        the `Student` instance (same as 8-class_to_json.py)
        If attrs is a list of strings, only attribute names contained in this
        list must be retrieved. Otherwise, all attributes must be retrieved
        Args:
            attrs (list): A list of attribute names to retrieve/represent.
        Returns:
            dict: The dictionary representation of the `Student` object
        """
        if type(attrs) == list and all(type(elem) == str for elem in attrs):
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}
        return self.__dict__
