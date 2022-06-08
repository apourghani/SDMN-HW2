from http.server import HTTPServer, BaseHTTPRequestHandler
import http.server
import cgi




class SimpleHTTPServer(BaseHTTPRequestHandler):
	GETOK = True
	def do_GET(self):

		if self.path == '/api/v1/status':
			if self.GETOK:
				self.send_response(200)
				self.send_header("Content-type", "application/json")
				self.end_headers()
				self.wfile.write(bytes('{"status": "OK"}'), "utf-8")
			else:
				self.send_response(200)
				self.send_header("Content-type", "application/json")
				self.end_headers()
				self.wfile.write(bytes('{"status": "not OK"}'), "utf-8")


	def do_POST(self):
		if self.path == '/api/v1/status':
			contentType, paramDict = cgi.parse_header(self.headers.get("Content-type"))
			paramDict["boundary"] = bytes(paramDict["boundary"], "utf-8") 		#Doubt???????????
			recContent = cgi.parse_multipart(self.rfile, paramDict)
			if recContent.get("status") == "not OK":
				self.send_response(201)
				self.send_header("Content-type", "application/json")
				self.end_headers()
				self.wfile.write(bytes('{"status": "not OK"}'), "utf-8")
				self.GETOK = False
				
			elif recContent.get("status") == "OK" and self.GETOK:
				self.send_response(201)
				self.send_header("Content-type", "application/json")
				self.end_headers()
				self.wfile.write(bytes('{"status": "not OK"}'), "utf-8")
				self.GETOK = True




def main():
	HOST = "localhost"
	PORT = 8000
	server_ip_port = (HOST, PORT) 
	server = HTTPServer(server_ip_port, SimpleHTTPServer)
	print("Server is running ....")
	server.serve_forever()
	
	



if __name__ == '__main__':
	main()















