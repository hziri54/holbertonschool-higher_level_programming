#!/usr/bin/python3
"""Définir une classe pour les objets"""


def is_same_class(obj, a_class):
    """Regarder si l'objet se trouve dans le meme endroit"""
    if type(obj) == a_class:
        return True
    return False
