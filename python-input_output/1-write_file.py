#!/usr/bin/python3
"""Fonction qui écrit une chaine de caractères"""


def write_file(filename="", text=""):
    """Écriture d'un fichier texte utf8"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
