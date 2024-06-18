#!/usr/bin/python3
"""Defines a class student"""


class Student:
    """Def class student"""

    def __init__(self, first_name, last_name, age):
        """init set for for student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionary representation of a Student instance"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__