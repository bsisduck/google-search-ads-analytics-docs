#!/usr/bin/env python3
"""Serve ./app on the first free port (tries 8800..8899)."""
import http.server, socketserver, os, socket

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def free_port(start=8800, end=8899):
    for p in range(start, end + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(("127.0.0.1", p)) != 0:   # nothing listening
                return p
    raise SystemExit("no free port in range")

class H(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):  # quieter
        pass
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, max-age=0")
        super().end_headers()

port = free_port()
with socketserver.TCPServer(("127.0.0.1", port), H) as httpd:
    print(f"SERVING http://localhost:{port}/  (Ctrl+C to stop)", flush=True)
    httpd.serve_forever()
