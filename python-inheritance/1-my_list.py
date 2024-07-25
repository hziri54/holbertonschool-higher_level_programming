#!/usr/bin/python3
"""Define a class MyList that inherits from list"""


class MyList(list):
    """Class MyList that inherits from list"""

    def print_sorted(self):
        """Print a list in ascending order"""
        print(sorted(self))
