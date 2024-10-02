#!/usr/bin/python3
"""Ajout chaine de caractère a la fin d'un codage"""


def append_write(filename="", text=""):
    """Ouvre le fichier en mode ajout et écrit le texte à la fin"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
