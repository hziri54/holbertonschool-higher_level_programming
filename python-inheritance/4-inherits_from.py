def inherits_from(obj, a_class):
    """Vérifie si l'objet est une instance d'une classe qui hérite (directement ou indirectement) 
    de la classe spécifiée (sans être une instance directe).
    
    Args:
        obj: L'objet à vérifier.
        a_class: La classe à comparer.
    
    Returns:
        True si l'objet est une instance d'une sous-classe de 'a_class', sinon False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
