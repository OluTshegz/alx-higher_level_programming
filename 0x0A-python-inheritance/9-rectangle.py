#!/usr/bin/python3
"""Defines a `Rectangle` that inherits from super/Parent class BaseGeometry.
(based on 8-rectangle.py)."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """represents/models a sub/child class `Rectangle` using BaseGeometry."""

    def __init__(self, width, height):
        """intializes an instance method of the new class `Rectangle` Object.
        Args:
            width (int): The width of the new `Rectangle`.
            height (int): The height of the new `Rectangle`."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of the Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns the Rectangle string representation"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
