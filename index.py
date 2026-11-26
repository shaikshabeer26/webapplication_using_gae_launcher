#print 'Content-Type: text/plain'
#print ' '
#print 'Assalamualikum'

from http.server import HTTPServer, BaseHTTPRequestHandler
import sys

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Assalamualikum\n")

if __name__ == '__main__':
    port = 8080
    print(f"Serving index.py at http://localhost:{port}")
    server = HTTPServer(('localhost', port), SimpleHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server.")
        sys.exit(0)
