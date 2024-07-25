#!/usr/bin/python3
"""Define a class Rectangle that inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a new Rectangle

        width : The width of the new rectangle
        height : The height of the new rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
