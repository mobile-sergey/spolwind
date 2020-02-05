from http.server import BaseHTTPRequestHandler


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        path = self.path
        if path == "/":
            path = "/index.html"

        if path == "/favicon.ico":
            self.set_headers('image/ico')
            file = open("../client/img/favicon.ico", 'rb')
            self.get_content(file, file.read())
        elif path.split("/")[1] == "img":
            self.set_headers('image/*,image/jpeg,image/png')
            file = open("../client" + path, 'rb')
            self.get_content(file, file.read())
        else:
            self.set_headers('text/html')
            try:
                file = open("../client" + path.split("?")[0], "r", encoding='utf-8')
            except FileNotFoundError:
                file = open("../client/errors/404.html", "r", encoding='utf-8')
            self.get_content(file, bytes(file.read(), "utf-8"))
        return

    def set_headers(self, content_type):
        self.send_response(200)
        self.send_header('Content-type', content_type)
        self.end_headers()
        return

    def get_content(self, file, content):
        self.wfile.write(content)
        file.close()




