import http.server
import json


class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        routes = {
            '/': (200, 'Hello, this is a simple API!', 'text/plain'),
            '/data': (200, json.dumps({"name": "John", "age": 30, "city": "New York"}), 'application/json'),
            '/status': (200, 'OK', 'text/plain'),
        }
        
        response = routes.get(self.path, (404, 'Not Found', 'text/plain'))
        self.send_response(response[0])
        self.send_header('Content-type', response[2])
        self.end_headers()
        self.wfile.write(response[1].encode())

    def do_POST(self):
        if self.path == '/data':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data)
                response = {"message": "Data received", "data": data}
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(response).encode())
            except json.JSONDecodeError:
                self.send_error(400, 'Bad Request: Invalid JSON')
        else:
            self.send_error(404, 'Not Found')


if __name__ == '__main__':
    httpd = http.server.HTTPServer(('', 8000), MyHandler)
    print("Server running on port 8000...")
    httpd.serve_forever()

