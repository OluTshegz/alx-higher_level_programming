#!/usr/bin/python3
"""class Square that defines a square by: (based on 0-square.py)"""


class Square:
    """Represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """ Initializing a new square.

        Args:
            size(int): size of the square
            position(int, int): position of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """gets the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """gets the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the position of the square"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                any(type(num) is not int or num < 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """Print the square with the # character"""
        if self.__size == 0:
            print()
            return

        for x in range(self.__position[1]):
            print()

        for x in range(self.__size):
            for y in range(self.__position[0]):
                print(" ", end="")
            for z in range(self.__size):
                print("#", end="")
            print()

    def __str__(self):
        """Printing a Square instance similar to my_print()"""
        if self.__size != 0:
            for x in range(self.__position[1]):
                print()

        for x in range(self.__size):
            for y in range(self.__position[0]):
                print(" ", end="")
            for z in range(self.__size):
                print("#", end="")
            if x != self.__size - 1:
                print()
        return("")
