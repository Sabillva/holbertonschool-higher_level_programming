import http.server
import json
import socketserver

class NewHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
         self.send_response(200)
         self.send_header('Content-type', 'text/plain')
         self.end_headers()
         self.wfile.write(b'Hello, this is a simple API!')
