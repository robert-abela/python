from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
from time import asctime
from list import list_files
from urllib.parse import unquote

hostName = "localhost"
hostPort = 80

def send_file(server, request_query):
    request_query = unquote(request_query) #hello%20bye.js -> hello bye.js
    try:
        file = open(request_query, "r")
        response_file = file.read()
    except FileNotFoundError:
        server.send_response(404)
        server.end_headers()
    else:
        server.send_response(200)
        server.send_header("Content-type", "text")
        server.end_headers()
        server.wfile.write(bytes(response_file, "utf-8"))

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        request_query = urlparse(self.path).path[1:] #remove /
        if (request_query == ''):
            request_query = 'index.html' #default response

        if request_query == "list":
            list_files(self)
        else:
            send_file(self, request_query)

if __name__ == "__main__":
    try:
        myServer = HTTPServer((hostName, hostPort), MyServer)
        print(asctime(), "Start - %s:%s" % (hostName, hostPort))
        myServer.serve_forever()
    except KeyboardInterrupt:
        myServer.server_close()
        print(asctime(), "Stop - %s:%s" % (hostName, hostPort))
