#!/usr/bin/python3
"""this module inherits from class `list`"""


class MyList(list):
    """subclass `MyList` inherits from `list`"""

    def print_sorted(self):
        """prints a sorted list, in ascending order"""
        print(sorted(self))
