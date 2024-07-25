#!/usr/bin/python3
"""Defines a class-checking function"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class

    returns:
        If obj is exactly an instance of a_class - True
        Otherwise - False
    """
    if type(obj) is a_class:
        return True
    return False
