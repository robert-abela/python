from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        if parsed.path == "/maltese":
          msg = "<html><body>Ghandi il-guh</body></html>"
        elif parsed.path == "/english":
          msg = "<html><body>I am hungry</body></html>"
        else:
          msg = "<html><body>???</body></html>"
        self.wfile.write(bytes(msg, "utf-8"))
try:
    myServer = HTTPServer(("localhost", 80), MyServer)
    myServer.serve_forever()
except KeyboardInterrupt:
    myServer.server_close()
