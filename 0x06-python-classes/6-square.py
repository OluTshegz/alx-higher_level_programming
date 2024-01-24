#!/usr/bin/python3
"""defines a class 'Square'"""


class Square:
    """represents a square blueprint"""
    def __init__(self, size=0, position=(0, 0)):
        """initializes a new square
        Args:
            size(int): size of the new square
            position(int): position of the new square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """gets the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
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
        if (type(value) is not tuple or
                len(value) != 2 or
                any(type(num) is not int or num < 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """returns the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints in stdout the square with the character '#'"""
        if self.__size == 0:
            print()
            return

        for x in range(self.__position[1]):
            print()

        for x in range(self.__size):
            for y in range(self.__position[0]):
                print(" ", end='')
            for z in range(self.__size):
                print("#", end='')
            print()
