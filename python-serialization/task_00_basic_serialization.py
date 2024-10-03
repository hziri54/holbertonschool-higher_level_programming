#!/usr/bin/python3
"""Convesion du dictionnaire en format JSON"""
import json

def serialize_and_save_to_file(data, filename):
   
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def load_and_deserialize(filename):
    """Le fichier JSON se transfome en dictionnaire python"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
