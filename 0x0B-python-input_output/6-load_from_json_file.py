#!/usr/bin/python3
"""This module defines a JSON file-reading function"""
import json


def load_from_json_file(filename):
    """Creates a Python object from a “JSON file”
    Args:
        filename (str): The file containing the object's JSON reprensentation.
    Returns:
        object: The associated Python object  represented in the JSON file."""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
