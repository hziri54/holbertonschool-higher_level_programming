#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Returns a list with True or False depending on whether each integer is divisible by 2."""
    return [num % 2 == 0 for num in my_list]
