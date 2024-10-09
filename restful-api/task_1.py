# Utilisation de `curl` pour interagir avec des API

`curl` est un outil de ligne de commande permettant de transférer des données via des protocoles comme HTTP et HTTPS. Cet outil est essentiel pour tester et interagir avec des APIs.

## Étapes essentielles :

1. **Installation**  
   Assurez-vous que `curl` est installé sur votre système.

2. **Vérification de l'installation**  
   Exécutez la commande suivante pour vérifier l'installation :  
   ```bash
   curl --version

    Récupération de données
    Pour obtenir une liste d'articles depuis une API, exécutez :

    bash

curl https://jsonplaceholder.typicode.com/posts

Obtenir les en-têtes HTTP
Pour récupérer uniquement les en-têtes, utilisez la commande suivante :

bash

curl -I https://jsonplaceholder.typicode.com/posts

Envoi de données avec une requête POST
Pour envoyer des données, utilisez la commande suivante :

bash

curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
