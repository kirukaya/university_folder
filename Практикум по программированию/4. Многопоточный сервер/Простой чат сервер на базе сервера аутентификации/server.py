import socket
import random 
import hashlib
import os, sys
from threading import Thread
import time
import copy


def print_logs(msg, clr = False):
	status = {True: 'w', False: 'a'}
	with open('logs.txt', status[clr], encoding='utf8') as file:
		print(msg, file = file)

def s_register(conn, addr):
	try:
		conn.send(f'регистрация'.encode())
		data = conn.recv(1024)
		login = data.decode()
		data = conn.recv(1024)
		passw = data.decode()

		# хеширование
		salt = os.urandom(32)
		key = hashlib.pbkdf2_hmac(
			'sha256',
			passw.encode('utf-8'),
			salt,
			100000
		)

		userinfo[addr[0]] = [login, salt+key]
		conn.send('успешно'.encode())
		with open('clients.txt', 'w') as file:
			print(userinfo, file = file)
	except:
		conn.send('что-то пошло не так'.encode())

def s_login(conn, addr):
	try:
		conn.send(f'логин'.encode())
		data = conn.recv(1024)
		login = data.decode()
		data = conn.recv(1024)
		passw = data.decode()

		# проверка пароля по ключу и хешу
		new_key = hashlib.pbkdf2_hmac(
			'sha256',
			passw.encode('utf-8'),
			userinfo[addr[0]][1][:32],
			100000
		)

		if new_key == userinfo[addr[0]][1][32:] and login == userinfo[addr[0]][0]:
			conn.send('успешно'.encode())
		else:
			conn.send('неправильные данные'.encode())
	except:
		conn.send('что-то пошло не так'.encode())


def checking_for_events():
	currentuserscopy = copy.deepcopy(currentusers)
	chatscopy = copy.deepcopy(chats)
	while True:
		# if currentusers != currentuserscopy:
		# 	for user, data in currentusers.items():
		# 		connaddr[data].send('новый пользователь'.encode())
		# 	currentuserscopy = copy.deepcopy(currentusers)
		if chatscopy != chats:
			for i, j in chats.items():
				for m, n in chatscopy.items():
					if i == m and j != n:
						upd = i
			for user, data in currentusers.items():
				connaddr[data].send(str(chats).encode())
			chatscopy = copy.deepcopy(chats)
		time.sleep(0.1)
		
		

def working_with_client(conn, addr):
	# логин или регистрация
	global connaddr
	try:
		if addr[0] in userinfo:
			s_login(conn, addr)
		else:
			s_register(conn, addr)
		
		connaddr = {addr: conn}
		currentusers[addr]=addr

		while True:
			data = conn.recv(1024) # слушаем действия пользователя
			if data.decode()[:7] == 'allchat':
				newstr = data.decode()[7:].strip()
				chats['allchat'].append([addr, newstr])
				print_logs(chats)
		print_logs(f'Отключение клиента {addr}...')
	except:
		print_logs(f'Отключение клиента {addr}...')


	

def waiting_for_clients():
	try:
		while True:
			conn, addr = sock.accept()
			print_logs(f'Подключение клиента {addr}...')
			t = Thread(target = working_with_client, args=(conn, addr))
			t.daemon = True
			t.start()
	except:
		print_logs('Остановка сервера...')
		conn.close()


def command_prompt():
	while True:
		command = input('>').split()
		if command[0] == 'shutdown':
			sys.exit()
		elif command[0] == 'help':
			print('''основные команды:
shutdown - выключить сервер
''')
		

if __name__ == '__main__':
	userinfo = {}
	with open('clients.txt', 'r') as file:
		for line in file.readlines():
			userinfo = eval(line)

	currentusers = {}
	sock = socket.socket()
	print_logs('Запуск сервера...', clr = True)

	chats = {'allchat': []}

	connaddr = {}

	port = 9090
	ready = False
	while not ready:
		try:
			sock.bind(('', port))
			ready = True
		except:
			pport = port
			port = random.randint(1000, 9999)
	print_logs(f'Прослушивание порта {port}...')
	sock.listen(0)
	
	Thread(target = waiting_for_clients, daemon = True).start()
	Thread(target = checking_for_events, daemon = True).start()

	command_prompt()