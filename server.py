import socketserver
import json
import shutil
import atexit

files = dict()

class MyTCPServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True

class MyTCPServerHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = json.loads(self.request.recv(1024).decode('UTF-8').strip())
        if 'type' in data:
            if data['type'] == "add":
                addFile(data['path'], data['filename'])
            elif data['type'] == "move":
                moveFile(data['path'], data['filename'])
            elif data['type'] == "remove":
                print("Remove file")
            
            
def moveFile(path, filename):
    for k in files.keys():
        if k in filename:
            shutil.move(path, files[k] + filename)
            print("Moving : " + path + " to :" + files[k] + filename)
            
def addFile(path, filename):
    print("Adding " + filename + " to " + path)
    files[filename] = path

def loadDict():
    return 0
    
def writeDict():
    return 0

server = MyTCPServer(('127.0.0.1', 13373), MyTCPServerHandler)
loadDict()
atexit.register(writeDict)
server.serve_forever()