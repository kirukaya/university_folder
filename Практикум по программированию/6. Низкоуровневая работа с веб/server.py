from datetime import datetime
import socket
import threading
import random
import json
import os
import re
import magic

def getConfig(filename = 'config.json'):
    with open(filename, 'r') as file:
        config = json.load(file)
    return config['port'], config['request_volume'], config['root']

def bindSocket(port):
    sock = socket.socket()
    while True:
        try: 
            sock.bind(('', port))
            print(f'Using port {port}')
            return sock
        except:
            port = random.randint(1024, 65535)

def http_response(content, request_date, addr, resource, http_response_code, content_type):
    content_length = len(content)
    log = [str(item) for item in [request_date, addr, resource, http_response_code]]
    log = "; ".join(log)
    with LOCK:
        with open(logfile, "a", encoding = "utf8") as logfl:
            logfl.write(log+"\n")
    response = f"""HTTP/1.1 {http_response_code}
Date: {str(datetime.now())[-6]}
Content-length: {content_length}
Server: SelfMadeServer v0.0.1
Content-type: {content_type}
Connection: retry-after

"""
    response = response.encode() + content
    return response

def resource_parser(request):
    request = request.split("\r\n")
    http_request = request[0].split()[1]
    request_path = re.split("[\\/]", http_request)
    if request_path == ["", ""]:
        request_path = ["index.html"]
    allowed = bool(re.search("\.(html|css|js|png|jpg|jpeg|pdf)$", request_path[-1]))
    return request_path, http_request, allowed

def request_reader(request):
    resource, http_path, allowed = resource_parser(request)
    resource = os.path.join(root, *resource)
    content_type = "text/html"
    if allowed:
        
        try:
            with open(resource, "rb") as contentfile:
                content = contentfile.read(1024*1024*16)
            response_code = "200 OK"
            mime = magic.Magic(mime=True)
            content_type = mime.from_file(resource)
        except:
            content = b""
            response_code = "404 Not Found"
    else:
        content = b""
        response_code = "403 Forbidden"
    return content, http_path, response_code, content_type

def clientThread(conn, addr):
    while True:
        request = conn.recv(request_volume).decode()
        request_date = str(datetime.now())[:-6]
        if not request:
            continue
        content, resource, response_code, content_type = request_reader(request)
        conn.send(http_response(content, request_date, addr, resource, response_code,content_type)) 

if __name__ == '__main__':
    LOCK = threading.Lock()
    logfile = 'log.txt'
    port, request_volume, root = getConfig()
    sock = bindSocket(port)
    sock.listen(5)
    while True:
        conn, addr = sock.accept()
        with LOCK: 
            print(f'User {addr} connected.')
        threading.Thread(target = clientThread, args = (conn, addr), daemon = True).start()
    conn.close()