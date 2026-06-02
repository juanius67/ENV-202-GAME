import json
import os
import http.server
import socketserver
import webbrowser
from urllib.parse import urlparse, parse_qs
import threading
import time
from datetime import datetime, timedelta
from datetime import timedelta

PORT = 8000
SAVE_FILE = 'save_data.json'

# Default save data
def get_default_save():
    return {
        "streak": 0,
        "high_score": 0,
        "last_played_date": ""
    }

def load_save_data():
    if not os.path.exists(SAVE_FILE):
        return get_default_save()
    try:
        with open(SAVE_FILE, 'r') as f:
            return json.load(f)
    except:
        return get_default_save()

def save_data(data):
    with open(SAVE_FILE, 'w') as f:
        json.dump(data, f, indent=4)

class GameRequestHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        parsed_path = urlparse(self.path)

        if parsed_path.path == '/api/load':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.end_headers()
            data = load_save_data()
            self.wfile.write(json.dumps(data).encode())
            return

        # Serve static files as usual
        return super().do_GET()

    def do_POST(self):
        parsed_path = urlparse(self.path)

        if parsed_path.path == '/api/save':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                new_data = json.loads(post_data.decode('utf-8'))

                # Load current save
                current_save = load_save_data()

                # Update High Score
                score = new_data.get('score', 0)
                if score > current_save['high_score']:
                    current_save['high_score'] = score

                # Update Streak (only increment once per day)
                today_str = datetime.now().strftime("%Y-%m-%d")
                if current_save['last_played_date'] == "":
                    current_save['streak'] = 1
                    current_save['last_played_date'] = today_str
                elif current_save['last_played_date'] != today_str:
                    yesterday_str = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
                    if current_save['last_played_date'] == yesterday_str:
                        current_save['streak'] += 1
                    else:
                        current_save['streak'] = 1
                    current_save['last_played_date'] = today_str

                save_data(current_save)

                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "success", "data": current_save}).encode())

            except Exception as e:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode())
            return

        self.send_response(404)
        self.end_headers()

def run_server():
    # To allow re-binding to the port quickly
    socketserver.TCPServer.allow_reuse_address = True

    with socketserver.TCPServer(("", PORT), GameRequestHandler) as httpd:
        print(f"Serving Metabolic Madness on http://localhost:{PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    # Start the server in a separate thread
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()

    # Wait a moment for server to start
    time.sleep(1)

    # Open the browser automatically
    print("Opening browser...")
    webbrowser.open(f"http://localhost:{PORT}/index.html")

    try:
        # Keep the main thread alive
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down server...")
