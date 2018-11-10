#!/usr/bin/env python
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import time
from list import htmlList

hostName = "localhost"
hostPort = 80
indexHTML = ""

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        request_query = urlparse(self.path).path
        if request_query == "/run":
            self.wfile.write(bytes(htmlList(), "utf-8"))
        else:
            self.wfile.write(bytes(indexHTML, "utf-8"))

if __name__ == "__main__":
    try:
        html = open("index.html", "r")
        indexHTML = html.read()
        myServer = HTTPServer((hostName, hostPort), MyServer)
        print(time.asctime(), "Start - %s:%s" % (hostName, hostPort))
        myServer.serve_forever()
    except FileNotFoundError:
        print(time.asctime(), "Start failed, index.html not found")
    except KeyboardInterrupt:
        myServer.server_close()
        print(time.asctime(), "Stop - %s:%s" % (hostName, hostPort))
