import socketserver
import json

class MyTCPServer(socketserver.ThreadingTCPServer):
	allow_reuse_address = True

class MyTCPServerHandler(socketserver.BaseRequestHandler):
	def handle(self):
		data = json.loads(self.request.recv(1024).decode('UTF-8').strip())
		if 'type' in data:
			if data['type'] == "add":
				addFile(data['path'], data['filename'])
			elif data['type'] == "move":
				moveFile(data['path', data['filename'])
			
def moveFile(path, filename):
	print(path + filename)
	
def addFile(path, filename):
	

		
		
server = MyTCPServer(('127.0.0.1', 13373), MyTCPServerHandler)
server.serve_forever()