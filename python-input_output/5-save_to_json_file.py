#!/usr/bin/python3
"""Fonction qui écrit un objet dans un fichier texte"""
import json


def save_to_json_file(my_obj, filename):
    """L'objet est écrit dans un fichier texte"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
