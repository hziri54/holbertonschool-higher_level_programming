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
