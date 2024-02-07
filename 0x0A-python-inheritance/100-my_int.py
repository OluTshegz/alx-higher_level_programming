#!/usr/bin/python3
"""this module defines a class `MyInt` that inherits from `int`."""


class MyInt(int):
    """inverts the `==` and `!=` operators."""

    def __eq__(self, value):
        """override == operator with != behavior.
        returns the boolean value"""
        return self.real != value

    def __ne__(self, value):
        """override != operator with == behavior.
        returns the boolean value"""
        return self.real == value
