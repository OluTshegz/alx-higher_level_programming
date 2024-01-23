#!/usr/bin/python3
"""defines a class 'Square'"""


class Square:
    """represents a square blueprint"""
    def __init__(self, size=0):
        """initializes a new square
        Args:
            size(int): size of the new square
        """
        self.size = size

    @property
    def size(self):
        """gets the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        # value must be an integer
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        # it should be greater than or equal to zero
        if value < 0:
            raise ValueError("size must be >= 0")

        # set the value of the Square if all goes well
        self.__size = value

    def area(self):
        """returns the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints in stdout the square with the character '#'"""
        if self.__size == 0:
            print() # print a newline only, when the size is zero

        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print()
