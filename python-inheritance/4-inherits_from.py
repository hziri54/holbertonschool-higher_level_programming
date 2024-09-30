#!/usr/bin/python3
"""Féfinir la fonction qui est héritée"""

def inherits_from(obj, a_class):
    """Regarder l'objet qui hérite de la classe"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
