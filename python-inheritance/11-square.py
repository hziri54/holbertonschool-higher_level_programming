#!/usr/bin/python3
"""Defines the Square class that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Defines a square and calculates its area"""

    def __init__(self, size):
        """Initialize a new square with a validated size"""
        
        self.integer_validator("size", size)
        self.__size = size
       
        super().__init__(size, size)

    def area(self):
        """Return the area of the square"""
        return self.__size * self.__size

    def __str__(self):
        """Return a string representation of the Square"""
        return f"[Square] {self.__size}/{self.__size}"
