import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
sock.connect(('IP-address', 9090))

while True:
	msg = input()
	#msg = "Hi!"
	if msg == 'exit':
		break
	sock.send(msg.encode())
	data = sock.recv(1024)
	print(f'data: {data.decode()}')
	
sock.close()
