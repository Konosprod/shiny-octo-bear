import socket
import json
import sys

IP = "127.0.0.1"
PORT = 13373

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))

def sendAdd(path, filename):
    
    data  = {"type" : "add", "path" : path, "filename" : filename}
    
    s.send(bytes(json.dumps(data), 'UTF-8'))

def sendRemove(filename):
    data = {"type" : "remove", "filename" : filename}
    print(data)
    s.send(bytes(json.dumps(data), 'UTF-8'))

def sendMove(path, filename):
    data  = {"type" : "move", "path" : path, "filename" : filename}
    
    s.send(bytes(json.dumps(data), 'UTF-8'))

    
if __name__ == "__main__":
    if sys.argv[1] == 'add':
        sendAdd(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'move':
        sendMove(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'remove':
        sendRemove(sys.argv[2])
        
    s.close()