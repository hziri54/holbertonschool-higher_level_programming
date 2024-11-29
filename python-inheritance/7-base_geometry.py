#!/usr/bin/python3
"""Defines class BaseGeometry with validation methods."""


class BaseGeometry:
    """Represents base geometry."""

    def area(self):
        """Raises an exception if not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if value is an integer and greater than 0."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
