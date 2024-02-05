#!/usr/bin/python3
"""A module with a class that models geometric
shapes with methods: area(), integer_validator()
(based on 6-base_geometry.py)."""


class BaseGeometry():
    """Definition of the BaseGeometry class
    Instance methods:
        area: raises an Exception with message
            'area() is not implemented'
        integer_validator: that validates value
            args: name, value
            Exceptions:
                TypeError: <name> must be an integer
                ValueError: <name> must be greater than 0"""
    def area(self):
        """a public instance method not implemented
        yet that raises an Exception with a message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name: str, value: int) -> None:
        """Performs validation of integer values.
        Args:
            name (str): The name of the object.
            value (int): The value of the object.
        Raises:
            TypeError: When the `value` given to the object is not an integer.
            ValueError: When the the `value` is less than or equal to zero."""
        if (type(value) is not int and type(value) != int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
