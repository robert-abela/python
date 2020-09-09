from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)

        if 'user' in params:
            user = params['user'][0] #there might be more than 1 value
        else:
            user = 'unknown user'

        msg = "<html><body>Hello "+user+"</body></html>"
        
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(msg, "utf-8"))
try:
    myServer = HTTPServer(("localhost", 80), MyServer)
    myServer.serve_forever()
except KeyboardInterrupt:
    myServer.server_close()
