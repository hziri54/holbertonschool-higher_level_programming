from http.server import BaseHTTPRequestHandler, HTTPServer

class My_SubClass(BaseHTTPRequestHandler):
    """
    sub class
    """
    def do_GET(self):
        """
        method do_get that handles GET requests
        """
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Bonjour, ceci est une API simple !')

# Utiliser My_SubClass au lieu de BaseHTTPRequestHandler
httpd = HTTPServer(('', 8000), My_SubClass)
print("Serveur en cours d'exécution sur le port 8000...")
httpd.serve_forever()
