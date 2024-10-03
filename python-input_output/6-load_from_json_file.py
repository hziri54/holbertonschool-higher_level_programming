#!/usr/bin/python3
"""Ecrire une fonction qui crée un objet a partir d'un fichier JSON"""
import json


def load_from_json_file(filename):
    """Création de l'objet a partir du fichier JSON"""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
