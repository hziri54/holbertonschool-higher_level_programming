#!/usr/bin/python3
"""Définition de la classe Rectangle"""

class Rectangle:
    """Représente un rectangle"""

    def __init__(self, largeur=0, hauteur=0):
        """
        Initialise un nouveau rectangle.

        Arguments:
        - largeur (int) : La largeur du rectangle.
        - hauteur (int) : La hauteur du rectangle.
        """
        self.largeur = largeur
        self.hauteur = hauteur

    @property
    def largeur(self):
        """Accède à la largeur du rectangle."""
        return self.__largeur

    @largeur.setter
    def largeur(self, valeur):
        if not isinstance(valeur, int):
            raise TypeError("La largeur doit être un entier")
        if valeur < 0:
            raise ValueError("La largeur doit être >= 0")
        self.__largeur = valeur

    @property
    def hauteur(self):
        """Accède à la hauteur du rectangle."""
        return self.__hauteur

    @hauteur.setter
    def hauteur(self, valeur):
        if not isinstance(valeur, int):
            raise TypeError("La hauteur doit être un entier")
        if valeur < 0:
            raise ValueError("La hauteur doit être >= 0")
        self.__hauteur = valeur

    def surface(self):
        """Calcule la surface du rectangle."""
        return self.__largeur * self.__hauteur
