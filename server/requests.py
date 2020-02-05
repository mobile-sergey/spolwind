from http.server import BaseHTTPRequestHandler


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        path = self.path
        if path == "/":
            path = "/index.html"

        if path == "/favicon.ico":
            f = open("../client/img/favicon.ico", 'rb')
            self.send_response(200)
            self.send_header('Content-type', 'image/ico')
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
        elif path.split("/")[1] == "img":
            f = open("../client" + path, 'rb')
            self.send_response(200)
            self.send_header('Content-type', 'image/*,image/jpeg,image/png')
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
        else:
            try:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                path = path.split("?")[0]
                file = open("../client" + path, "r", encoding='utf-8')
                message = file.read()
            except FileNotFoundError:
                file = open("../client/errors/404.html", "r", encoding='utf-8')
                message = file.read()
            file.close()

            self.wfile.write(bytes(message, "utf-8"))
        return
