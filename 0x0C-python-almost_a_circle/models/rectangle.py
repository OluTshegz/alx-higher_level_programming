#!/usr/bin/python3
"""This module contains class Rectangle and imports Base"""
from models.base import Base


class Rectangle(Base):
    """A subclass of the Bass class that represent a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Is the class constructor
        Args:
            width (int): The initiation value of the width of the rectangle
            height (int): The initiation value of the height of the rectangle
            x (int): The initiation value of the x of the rectangle
            y (int): The initiation value of the y of the rectangle
            id (int): The initiation value of the id of the rectangle

        Raises:
        TypeError: If width, height, x, or y is not integer
        ValueError: If width or height less that or equal to 0 or
        x or y less than 0
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the instance attribute (width)"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the instance attribute (width)
        Args:
            value: Is the value that will be asigned to width attribute

        Raises:
        TypeError: If (value) ss not an integer
        ValueError: If (value) is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the instance attribute (height)"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the instance attribute (height)
        Args:
            value: Is the value that will be asigned to height attribute

        Raises:
        TypeError: If (value) ss not an integer
        ValueError: If (value) is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for the instance attribute (x)"""
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the instance attribute (x)
        Args:
            value: Is the value that will be asigned to x attribute

        Raises:
        TypeError: If (value) ss not an integer
        ValueError: If (value) is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for the instance attribute (y)"""
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for the instance attribute (y)
        Args:
            value: Is the value that will be asigned to y attribute

        Raises:
        TypeError: If (value) ss not an integer
        ValueError: If (value) is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints the rectangle using (#)"""
        for a in range(self.y):
            print()
        for i in range(self.__height):
            print(" " * self.x, end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self) -> str:
        """Returns the string representation of the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """Assigns new value to each attribute"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
