#!/usr/bin/env python3

import http.server
import socketserver

handler = http.server.SimpleHTTPRequestHandler
#������ �� ����� 1234

with socketserver.TCPServer(("", 1234), handler) as httpd:
    #������ ����� ����������� ���������, ������ �������� �� �������
    httpd.serve_forever()