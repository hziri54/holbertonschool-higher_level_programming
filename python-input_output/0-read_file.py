#!/usr/bin/python3
"""Fonction qui lit un fichier texte"""


def read_file(filename=""):
    """Le fichier texte est lu"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
