#!/usr/bin/env python3

import http.server
import socketserver

handler = http.server.SimpleHTTPRequestHandler
#—ервер на порте 1234

with socketserver.TCPServer(("", 1234), handler) as httpd:
    #—ервер будет выполн€тьс€ посто€нно, ожида€ запросов от клиента
    httpd.serve_forever()