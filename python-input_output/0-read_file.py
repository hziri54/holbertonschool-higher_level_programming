#!/usr/bin/python3
"""Define file reading function."""


def read_file(filename=""):
    """Print the content of read"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")