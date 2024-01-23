#!/usr/bin/python3
"""defines a class 'Square'"""


class Square:
    """represents a square blueprint"""
    def __init__(self, size):
        """initializes a new square
        Args:
            size(int): size of the new square
        """
        self.__size = size
