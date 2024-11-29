#!/usr/bin/python3
"""Defines a square-printing function."""


def print_square(size):
    """Print a square with # """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
