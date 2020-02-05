from http.server import HTTPServer
import requests

server = HTTPServer(("", 8000), requests.RequestHandler)
print("Server working...")
server.serve_forever()
