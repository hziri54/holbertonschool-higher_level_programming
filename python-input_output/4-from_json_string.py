#!/usr/bin/python3
"""returns an object from a JSON string"""
import json


def from_json_string(my_str):
    """returns an object"""
    return json.loads(my_str)