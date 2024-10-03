#!/usr/bin/python3
"""Ecrire la classe student"""
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Creation de la classe student"""
        return self.__dict__
