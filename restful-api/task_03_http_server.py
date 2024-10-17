import http.server
import json


class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Route principale "/"
        if self.path == '/':
            self.send_response(200)  # Code 200 OK
            self.send_header('Content-type', 'text/plain')  # Type de contenu: texte brut
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')  # Réponse texte

        # Route "/data" : renvoyer des données JSON
        elif self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)  # Code 200 OK
            self.send_header('Content-type', 'application/json')  # Type de contenu: JSON
            self.end_headers()
            # Convertir le dictionnaire Python en JSON et l'envoyer
            self.wfile.write(json.dumps(data).encode('utf-8'))

        # Route "/status" : renvoyer le statut de l'API
        elif self.path == '/status':
            self.send_response(200)  # Code 200 OK
            self.send_header('Content-type', 'text/plain')  # Type de contenu: texte brut
            self.end_headers()
            self.wfile.write(b'OK')  # Réponse texte: OK

        # Route non définie (404 Not Found)
        else:
            self.send_response(404)  # Code 404 Not Found
            self.send_header('Content-type', 'application/json')  # Type de contenu: JSON
            self.end_headers()
            # Renvoyer une erreur en JSON
            error_message = {"error": "404 Not Found"}
            self.wfile.write(json.dumps(error_message).encode('utf-8'))


if __name__ == '__main__':
    # Serveur HTTP sur le port 8080
    server_address = ('', 8080)  # Assurez-vous que le port n'est pas occupé
    httpd = http.server.HTTPServer(server_address, MyHandler)
    print("Serving on port 8080...")
    httpd.serve_forever()

