import socket
from threading import Thread
import sys
import time

def workingWithClients(conn, addr):
	global logs
	msg = ''
	try:
		while True:
			data = conn.recv(1024)
			if not data:
				break
			msg += data.decode()
			conn.send(data)

			logs.append({addr:msg})

		conn.close()
	except:
		pass

def checkingForClients():
	while True:
		try:
			sock = socket.socket()
			sock.bind(('', 9090))
			sock.listen(0)
			conn, addr = sock.accept()
			if not paused:
				Thread(target=workingWithClients, args=[conn,addr]).start()
		except:
			pass
def main():
	global paused, logs
	logs = []
	paused = False
	while True:
		print('commands: stop, unpause, pause, clrlogs, logs')
		if paused:
			print('status: paused')
		else:
			print('status: available')
		s = input('>')
		if 'stop' in s or 'exit' in s: 
			sys.exit()
		elif 'unpause' in s: paused = False
		elif 'pause' in s: paused = True 
		elif 'clrlogs' in s or 'clearlogs' in s: 
			logs = []
			print('logs were cleared!')
		elif 'logs' in s: print(logs)
		print()

if __name__ == '__main__':
	t = Thread(target=checkingForClients)
	t.daemon = True
	t.start()
	main()
input()
