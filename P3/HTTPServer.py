from http.server import HTTPServer, BaseHTTPRequestHandler
import http.server
import cgi
import json

#this variable specifies GET function output
GETOK = True

class SimpleHTTPServer(BaseHTTPRequestHandler):
	def do_GET(self):
		global GETOK
		if self.path == '/api/v1/status':
			print(GETOK)
			if GETOK:
				self.send_response(200)
				self.send_header("Content-type", "application/json")
				self.end_headers()
				self.wfile.write(bytes(json.dumps({"status":'OK'},), 'utf-8'))
			else:
				self.send_response(201)
				self.send_header("Content-type", "application/json")
				self.end_headers()
				self.wfile.write(bytes(json.dumps({"status":'not OK'},), 'utf-8'))
	def do_POST(self):
		global GETOK
		if self.path =="/api/v1/status":
			content_length = int(self.headers['Content-Length'])
			content = self.rfile.read(content_length)
			if content.decode('UTF-8')[8:10] == "OK":
				GETOK = True
				self.send_response(200)
				self.send_header("Content-type", "application/json")
				self.end_headers()
				self.wfile.write(bytes(json.dumps({"status":'OK'}), 'utf-8'))
				
				
			elif str(content.decode("utf-8"))[8:10] == "no":
				GETOK = False
				self.send_response(201)
				self.send_header("Content-type", "application/json")
				self.end_headers()
				self.wfile.write(bytes(json.dumps({"status":'not OK'}), 'utf-8'))
				


def main():
	PORT = 8000

	print("Server is running on port 8000 ....")
	with HTTPServer(("",PORT),SimpleHTTPServer) as server:
		server.serve_forever()
	

if __name__ == '__main__':
	main()





