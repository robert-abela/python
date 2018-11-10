import os, sys

def list_files(server):
    server.send_response(200)
    server.send_header("Content-type", "text/html")
    server.end_headers()
    fullList = os.listdir('.')

    html = "<html><body><ol>"
    for item in fullList:
        if os.path.isfile(item) and item.endswith('.py'):
            html = html + "<li><a href=" + item + " >" + item + "</a></li>"
    html + "</ol></body></html>"

    server.wfile.write(bytes(html, "utf-8"))

