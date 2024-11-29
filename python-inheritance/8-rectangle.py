#!/usr/bin/python3
"""Defines the Rectangle class that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Defines a rectangle and calculates its area"""

    def __init__(self, width, height):
        """Initialize a new rectangle with validated width and height"""
        
        # Validate width and height using the integer_validator method from BaseGeometry
        self.integer_validator("width", width)
        self.__width = width
        
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """Return a string representation of the Rectangle"""
        return f"[Rectangle] {self.__width} / {self.__height}"

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

