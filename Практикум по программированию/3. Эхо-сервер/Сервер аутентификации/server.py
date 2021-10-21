import socket
import random 
import hashlib
import os

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

def waiting_for_client():
	try:
		while True:
			conn, addr = sock.accept()
			print(f'Подключение клиента {addr}...')

			if addr[0] in userinfo:
				s_login(conn, addr)
			else:
				s_register(conn, addr)
			print('Отключение клиента...')
	except:
		print('Остановка сервера...')
		conn.close()

if __name__ == '__main__':
	userinfo = {}
	with open('clients.txt', 'r') as file:
		for line in file.readlines():
			userinfo = eval(line)

	sock = socket.socket()
	print('Запуск сервера...')

	port = 9090
	ready = False
	while not ready:
		try:
			sock.bind(('', port))
			ready = True
		except:
			pport = port
			port = random.randint(1000, 9999)
	print(f'Прослушивание порта {port}...')
	sock.listen(0)
	waiting_for_client()