#!/usr/bin/python3
"""Module to find the max integer in a list"""

def max_integer(lst=[]):
    """Function to find and return the max integer in a list of integers.
    If the list is empty, the function returns None.
    """
    if len(lst) == 0:
        return None  # Retourne None si la liste est vide
    
    result = lst[0]  # Initialisation du résultat avec le premier élément de la liste
    
    for i in range(1, len(lst)):  # Itération à partir du deuxième élément
        if lst[i] > result:
            result = lst[i]  # Mise à jour du résultat si un élément plus grand est trouvé
    
    return result  # Retourne la valeur maximale trouvée
