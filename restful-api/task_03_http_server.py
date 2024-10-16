import http.server
import json
import socketserver

class NewHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
         self.send_response(200)