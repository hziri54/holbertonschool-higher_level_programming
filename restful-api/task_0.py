# Différences entre HTTP et HTTPS

# HTTP :
# - HTTP ne chiffre pas les données échangées entre le client (navigateur) et le serveur. 
#   Cela signifie que tout ce qui est transmis (comme les mots de passe) peut être intercepté.
# - Utilise le port 80.
# - Pas de certificat nécessaire, donc aucune garantie d'identité ou de sécurité.
# - Exemple : Utilisé pour des sites sans informations sensibles (blogs, pages d'information).

# HTTPS :
# - HTTPS ajoute un chiffrement via SSL/TLS, rendant les données illisibles par des attaquants.
# - Utilise le port 443.
# - Nécessite un certificat SSL/TLS pour garantir la sécurité et l'identité du serveur.
# - Exemple : Utilisé pour des sites bancaires, de commerce en ligne, ou tout site manipulant des données sensibles.

# En résumé : HTTPS protège la connexion en chiffrant les données, tandis que HTTP transmet les informations en clair.


# Structure d’une requête et réponse HTTP :

# Requête HTTP : elle est envoyée du client (navigateur) au serveur et contient :
# - Méthode (GET, POST, etc.)
# - URL de la ressource demandée
# - Version HTTP (ex : HTTP/1.1)
# - En-têtes (Headers) avec des infos comme l'identité du client, types de contenu, etc.
# - Corps (Body) : Présent dans certaines méthodes (ex : POST) pour envoyer des données.

# Exemple de requête :
'''
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
'''

# Réponse HTTP : elle est renvoyée par le serveur et contient :
# - Version HTTP (ex : HTTP/1.1)
# - Code de statut (ex : 200 OK, 404 Not Found)
# - En-têtes (Headers) avec des infos comme le type de contenu, date, etc.
# - Corps (Body) : La ressource demandée (ex : HTML de la page).

# Exemple de réponse :
'''
HTTP/1.1 200 OK
Date: Sun, 06 Oct 2024 10:00:00 GMT
Content-Type: text/html
Content-Length: 1234

<html>
  <body>...</body>
</html>
'''


# Méthodes HTTP courantes :

# 1. GET :
#    - Sert à récupérer des informations du serveur sans modifier la ressource.
#    - Utilisation : Demander une page web, obtenir des données via une API.

# 2. POST :
#    - Envoie des données au serveur pour qu'elles soient traitées (souvent via formulaire).
#    - Utilisation : Soumettre des données de formulaire d'inscription.

# 3. PUT :
#    - Remplace ou met à jour une ressource existante sur le serveur.
#    - Utilisation : Mettre à jour des informations utilisateur.

# 4. DELETE :
#    - Supprime une ressource sur le serveur.
#    - Utilisation : Supprimer un compte ou une publication.


# Codes de statut HTTP courants :

# 1. 200 OK :
#    - La requête a réussi et le serveur retourne la ressource demandée.
#    - Scénario : Accéder à une page web existante.

# 2. 301 Moved Permanently :
#    - La ressource a été déplacée définitivement vers une nouvelle URL.
#    - Scénario : Redirection d'une page vers une nouvelle adresse.

# 3. 400 Bad Request :
#    - La requête envoyée est incorrecte ou mal formée.
#    - Scénario : Une erreur lors de la soumission d'un formulaire mal rempli.

# 4. 404 Not Found :
#    - La ressource demandée n'a pas été trouvée sur le serveur.
#    - Scénario : Accéder à une URL qui n'existe pas.

# 5. 500 Internal Server Error :
#    - Le serveur a rencontré une erreur interne inattendue.
#    - Scénario : Problème de configuration ou bug côté serveur.
