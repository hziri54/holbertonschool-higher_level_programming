#!/usr/bin/python3
"""Defines a rectangles"""


class Rectangle:
    """Define rectangle."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a rectangle."""
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """set width of rectange"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """set height of rectange"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return perimeter of rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
    
    def __str__(self):
        """Print rectangle with #"""
        if self.__width == 0 or self.__height == 0:
            return("")

        rect = []
        for i in range(self.__height):
             [rect.append('#') for j in range(self.__width)]
             if i != self.__height - 1:
                 rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """return string of rectangle"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)
     
    def __del__(self):
        """print mess for del of rectange"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

