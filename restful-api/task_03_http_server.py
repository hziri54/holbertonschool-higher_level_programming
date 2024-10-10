#!/usr/bin/python3
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Définir la réponse pour différents endpoints
        if self.path == '/':
            # Page d'accueil simple
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Bonjour, ceci est une API simple !")

        elif self.path == '/data':
            # Renvoyer un JSON pour le chemin /data
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == '/status':
            # Endpoint /status pour vérifier l'état de l'API
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            # Gérer les endpoints non définis
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("Endpoint non trouvé")

def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print("Serveur en cours d'exécution sur le port 8000...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
