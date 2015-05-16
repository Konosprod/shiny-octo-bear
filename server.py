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
                removeFile(data['filename'])
        
def removeFile(filename):
    if filename in files.keys():
        files.pop(filename)
        
def moveFile(path, filename):
    for k in files.keys():
        if k in filename:
            shutil.move(path, files[k] + filename)
            print("Moving : '" + path + "' to : '" + files[k] + filename + "'")
            
def addFile(path, filename):
    print("Adding '" + filename + "' to '" + path + "'")
    files[filename] = path

def loadDict():
    global files
    try:
        fp = open('dict.txt', 'r')
        
        try:
            files = json.load(fp)
            fp.close()  
        except ValueError:
            print("Error loading dict.txt, it may be empty")
            
    except FileNotFoundError:
        fp = open('dict.txt', 'w')
        fp.close()
    
def writeDict():
    with open('dict.txt', 'w') as fp:
        json.dump(files, fp)
        fp.close()
        

server = MyTCPServer(('127.0.0.1', 13373), MyTCPServerHandler)
loadDict()
atexit.register(writeDict)
server.serve_forever()