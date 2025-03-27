from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):  # Corrected method name
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Hello World")

def main():
    server = HTTPServer(('', 1223), MyHandler)
    print("Started WebServer on port 1223...")
    print("Press ^C to quit WebServer.")

    server.serve_forever()

if __name__ == "__main__":
    main()
