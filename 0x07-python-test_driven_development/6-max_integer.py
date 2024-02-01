#!/usr/bin/python3
"""Task 5. Max integer - Unittest:
    This module has one function
    that prints the max integer
    in a list of integers"""
"""Module to find the max integer in a list"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        Args:
            list (list): a list of integers
        Returns:
            None if the list is empty"""

    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
