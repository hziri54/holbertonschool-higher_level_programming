#!/usr/bin/python3
"""Fonction qui renvoi la présentation JSON"""
import json


def from_json_string(my_str):
    """Réception de la présentarion JSON"""
    return json.loads(my_str)
