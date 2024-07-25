#!/usr/bin/python3
"""Defines a class-checking function"""


def inherits_from(obj, a_class):
    """Check if an object is an instance or inherited instance of a class

    Returns:
        If obj is an instance or inherited instance of a_class - True
        Otherwise - False
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
