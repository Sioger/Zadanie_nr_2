import http.server
import socketserver
import logging
from datetime import datetime
import pytz

PORT = 8000
AUTHOR = "Jan Kowalski"

# Set up logging
logging.basicConfig(filename='server.log', level=logging.INFO)
logging.info(f"Server started at {datetime.now()} by {AUTHOR} on port {PORT}")

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        client_ip = self.client_address[0]
        client_timezone = pytz.timezone('Etc/UTC')  # Default to UTC, can be adjusted based on IP
        client_time = datetime.now(client_timezone)
        
        response = f"""
        <html>
        <body>
        <h1>Client IP: {client_ip}</h1>
        <h2>Current Date and Time in your timezone: {client_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')}</h2>
        </body>
        </html>
        """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    logging.info(f"Serving at port {PORT}")
    httpd.serve_forever()
