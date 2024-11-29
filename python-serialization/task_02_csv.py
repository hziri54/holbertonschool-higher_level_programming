#!/usr/bin/env python3
import csv
import json

def convert_csv_to_json(csv_filename):
    try:
        # Ouvrir le fichier CSV
        with open(csv_filename, mode='r') as csv_file:
            # Créer un lecteur CSV avec DictReader
            csv_reader = csv.DictReader(csv_file)
            
            # Convertir chaque ligne du CSV en dictionnaire et les ajouter à une liste
            data = [row for row in csv_reader]
            
            # Ouvrir (ou créer) un fichier JSON pour écrire les données
            with open('data.json', mode='w') as json_file:
                # Sérialiser la liste de dictionnaires en JSON et l'écrire dans le fichier
                json.dump(data, json_file, indent=4)
        
        # Si tout se passe bien, retourner True
        return True
    
    except FileNotFoundError:
        # Si le fichier CSV n'est pas trouvé, retourner False
        print(f"Error: The file {csv_filename} was not found.")
        return False
