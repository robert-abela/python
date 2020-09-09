from http.server import BaseHTTPRequestHandler, HTTPServer

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><body>Hello!</body></html>", "utf-8"))

myServer = HTTPServer(("localhost", 80), MyServer)
myServer.serve_forever()
