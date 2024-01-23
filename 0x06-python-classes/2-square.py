#!/usr/bin/python3
"""defines a class 'Square'"""


class Square:
    """represents a square blueprint"""
    def __init__(self, size=0):
        """initializes a new square
        Args:
            size(int): size of the new square
        """
        # size must be an integer
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        # it should be greater than or equal to zero
        if size < 0:
            raise ValueError("size must be >= 0")

        # set the size of the Square if all goes well
        self.__size = size
