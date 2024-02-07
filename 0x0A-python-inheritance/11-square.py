#!/usr/bin/python3
"""Defines a `Square` that inherits from super/Parent class Rectangle.
(based on 10-square.py)."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represents/models a sub/child class `Square` using Rectangle"""

    def __init__(self, size):
        """initializes an instance method of the new class `Square` Object.
        Args:
            size (int): The size of the new Square."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
