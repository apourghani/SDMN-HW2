from http.server import HTTPServer , BaseHTTPRequestHandler
import json

isok=True

class WebServerHandler(BaseHTTPRequestHandler):
       
    def do_GET(self):
        global isok
        if self.path=='/api/v1/status':   
        	if isok==True:
            		self.send_response(200)
            		self.send_header('Content-type', 'application/json')
            		self.end_headers()
            		response= {"status":'ok'}
            		self.wfile.write(bytes(json.dumps(response, 	ensure_ascii=False), 'utf-8'))
        	else:
            		self.send_response(201)
            		self.send_header('Content-type', 'application/json')
            		self.end_headers()
            		response= {"status":'not ok'}
            		self.wfile.write(bytes(json.dumps(response, ensure_ascii=False), 'utf-8'))
           
       
    def do_POST(self):
        global isok
        if self.path=='/api/v1/status':
        	content_length = int(self.headers['Content-Length'])
        	post_data = self.rfile.read(content_length)
        	s=post_data.decode('UTF-8');
        	a=s.find("not ok")
        	if a>=0:
            		response = {
               	 	'status':'not ok'
               	 	}
            		isok=False
            		self.send_response(201)
            		self.send_header('Content-type', 'application/json')
            		self.end_headers()
            		self.wfile.write(bytes(json.dumps(response, 				ensure_ascii=False), 'utf-8'))
        	else:
            		response = {
               		 'status':'ok'
               		 }
            		isok=True
            		self.send_response(200)
            		self.send_header('Content-type', 'application/json')
            		self.end_headers()
            		self.wfile.write(bytes(json.dumps(response, 				ensure_ascii=False), 'utf-8'))
       
        	return
	

port = 8000
server = HTTPServer(('localhost', port), WebServerHandler)
print("Web server is running on port {}".format(port))
server.serve_forever()
server.server_close()
