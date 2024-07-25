#!/usr/bin/python3
"""Define a class BaseGeometry"""


class BaseGeometry:
    """Class BaseGeometry"""

    def area(self):
        """Public instance method that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
