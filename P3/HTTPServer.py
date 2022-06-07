from http.sever import HTTPServer, BaseHTTPRequestHandler

HOST = "127.0.0.1"
PORT = 8000


class SimpleHTTPServer(BaseHTTPRequestHandler):
	GETOK = True
	def do_GET(self):
		if self.path == '/api/v1/status':
			if self.GETOK:
				self.send_response(200)
				self.send_header("Content-type", "application/json")
				self.end_headers()
				self.wfile.write(bytes('{"status": "OK"}'), "utf-8"))
			else:
				self.send_response(201)
				self.send_header("Content-type", "application/json")
				self.end_headers()
				self.wfile.write(bytes('{"status": "not OK"}'), "utf-8"))
				

def do_POST(self):
		if self.path == '/api/v1/status':
			self.send_response(200)
			self.send_header("Content-type", "application/json")
			self.end_headers()
			self.wfile.write(bytes('{"status": "OK"}'), "utf-8"))



server = HTTServer((HOST, PORT), SimpleHTTPServer)


