#!/usr/bin/python3
"""Fonction qui renvoi la structure de données du dictionnaire"""


def class_to_json(obj):
    """Reception de la tructure de données"""
    return obj.__dict__
