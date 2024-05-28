#!/usr/bin/python3
"""Defines write-counting function"""


def write_file(filename="", text=""):
    """Write string utf8 text file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)