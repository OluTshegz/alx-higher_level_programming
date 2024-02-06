#!/usr/bin/python3
"""This module defines a class Student"""


class Student:
    """represents the Student class"""
    def __init__(self, first_name, last_name, age):
        """initializes a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """gets/retrieves a dictionary representation of
        the Student instance (same as 8-class_to_json.py)"""
        return self.__dict__
