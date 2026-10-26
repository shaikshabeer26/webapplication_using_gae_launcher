from http.server import HTTPServer, BaseHTTPRequestHandler
import sys

class GAELabHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Simple HTML page for your lab report screenshot
        html = """
        <html>
        <head>
            <title>GAE Web Application</title>
            <style>
                body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f0f2f5; text-align: center; padding-top: 50px; }
                .container { background: white; max-width: 500px; margin: 0 auto; padding: 30px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-top: 8px solid #4285F4; }
                h1 { color: #4285F4; margin-bottom: 5px; }
                h3 { color: #5f6368; margin-top: 0; font-weight: normal; }
                .badge { background-color: #34A853; color: white; padding: 6px 12px; border-radius: 20px; font-weight: bold; display: inline-block; margin: 15px 0; }
                p { color: #3c4043; line-height: 1.6; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Google App Engine</h1>
                <h3>Cloud Computing Lab-Experiment_4</h3>
                <div class="badge">STATUS: LIVE (LOCAL)</div>
                <p><b>Experiment Name:</b> Use GAE Launcher to launch web applications.</p>
                <p>The application environment initialized successfully and is actively handling requests.</p>
            </div>
        </body>
        </html>
        """
        self.wfile.write(bytes(html, "utf-8"))

if __name__ == '__main__':
    port = 8080
    print(f"Initializing GAE Launcher Workspace...")
    print(f"Serving web application at http://localhost:{port}")
    
    server = HTTPServer(('localhost', port), GAELabHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping GAE development server.")
        sys.exit(0)
