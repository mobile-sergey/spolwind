from http.server import BaseHTTPRequestHandler


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        message = "Сервер онлайн..."
        self.wfile.write(bytes(message, "cp1251"))
        return message
