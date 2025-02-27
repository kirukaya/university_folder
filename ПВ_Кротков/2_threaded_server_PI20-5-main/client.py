import socket
import time

while True:
    input('press ENTER to connect')
    sock = socket.socket()
    sock.setblocking(1)
    sock.connect(('26.68.165.46', 9090))

    msg = input('msg: ')
    try:
        sock.settimeout(2)
        sock.send(msg.encode())
        data = sock.recv(1024)
        sock.close()
        print(f'your message: {data.decode()}', end = '\n\n')

    except:
        print('timeout exception, server on pause', end = '\n\n')

