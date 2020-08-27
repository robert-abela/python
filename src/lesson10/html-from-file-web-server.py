from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
hostPort = 80
indexHTML = ""

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(indexHTML, "utf-8"))

if __name__ == "__main__":
    try:
        html = open("index.html", "r")
        indexHTML = html.read()
        myServer = HTTPServer((hostName, hostPort), MyServer)
        myServer.serve_forever()
    except FileNotFoundError:
        print(asctime(), "Start failed, index.html not found")
