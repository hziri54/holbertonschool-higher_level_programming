#!/usr/bin/python3
"""Define a class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a class Square"""

    def __init__(self, size):
        """Initialize a new Square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the current area of the square"""
        return (self.__size * self.__size)

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return ("[Square] {}/{}".format(self.__size, self.__size))
