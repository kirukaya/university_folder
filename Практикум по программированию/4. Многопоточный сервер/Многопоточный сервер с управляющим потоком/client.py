import socket
import time

yourIpAdress = 'X.X.X.X'

while True:
    input('press ENTER to connect')
    sock = socket.socket()
    sock.setblocking(1)
    sock.connect((yourIpAdress, 9090))

    msg = input('msg: ')
    try:
        sock.settimeout(2)
        sock.send(msg.encode())
        data = sock.recv(1024)
        sock.close()
        print(f'your message: {data.decode()}', end = '\n\n')

    except:
        print('timeout exception, server on pause', end = '\n\n')