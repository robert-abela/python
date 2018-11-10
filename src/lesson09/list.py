import os, sys

def htmlList():
    html = "<html><body><ol>"
    fullList = os.listdir('.')
    for item in fullList:
        if os.path.isfile(item):
            html = html + "<li>" + item + "</li>"

    return html + "</ol></body></html>"
