import http.server
import socketserver
from http import HTTPStatus


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(b'Hello World!')


httpd = socketserver.TCPServer(('', 8000), Handler)
print('Starting HTTP server')
httpd.serve_forever()
