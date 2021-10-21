import socket
import random 
	
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

try:
	while True:
		conn, addr = sock.accept()
		print(f'Подключение клиента {addr}')
		if addr[0] in userinfo:
			print(f'Имя клиента - {userinfo[addr[0]]}.')
			print('Отправка данных клиенту...')
			conn.send(f'Здравствуйте, {userinfo[addr[0]]}'.encode())
		else:
			print('Отправка данных клиенту...')
			conn.send(f'Здравствуйте, введите ваше имя.'.encode())
			print('Ожидание ответа от клиента...')
			data = conn.recv(1024)
			print(f'Клиент отправил: {data.decode()}')
			userinfo[addr[0]] = data.decode()
			with open('clients.txt', 'w') as file:
				print(userinfo, file = file)
		print('Отключение клиента...')
except:
	print('Остановка сервера...')
	conn.close()