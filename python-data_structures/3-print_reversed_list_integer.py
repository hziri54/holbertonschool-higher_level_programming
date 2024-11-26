#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in reverse order."""
    if my_list:
        for number in reversed(my_list):
            print("{:d}".format(number))
