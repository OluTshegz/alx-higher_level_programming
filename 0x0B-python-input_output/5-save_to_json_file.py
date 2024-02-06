#!/usr/bin/python3
"""This module defines a JSON file-writing function"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation
    Args:
        my_obj (object): The Python object to write.
        filename (str): The name of the file to write to."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
