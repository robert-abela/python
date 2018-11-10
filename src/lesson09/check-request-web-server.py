from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

hostName = "localhost"
hostPort = 80
indexHTML = ""

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        request_query = urlparse(self.path).path
        if request_query == "/stop":
            exit()
        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(indexHTML, "utf-8"))

try:
    html = open("index.html", "r")
    indexHTML = html.read()
    myServer = HTTPServer((hostName, hostPort), MyServer)
    myServer.serve_forever()
except FileNotFoundError:
    print("Start failed, index.html not found")
except KeyboardInterrupt:
    myServer.server_close()
