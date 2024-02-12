#!/usr/bin/python3
"""This module contains class Square and imports Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A subclass of the Rectangle class that represent a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        Is the class constructor
        Args:
            size (int): The initiation value of the size of the square
            x (int): The initiation value of the x of the square
            y (int): The initiation value of the y of the square
            id (int): The initiation value of the id of the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Returns the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the size of the square
        Args:
            value (int): Is the value to assign to the size of the square
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self) -> str:
        """Returns the string representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    def update(self, *args, **kwargs):
        """Assigns new value to each attribute"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
