import socket

sock = socket.socket()
print('Запуск сервера...')
sock.bind(('', 9090))
print('Прослушивание порта...')
sock.listen(0)
conn, addr = sock.accept()
print(f'Подключение клиента {addr}')

print('Прием данных от клиента...')
while True:
	data = conn.recv(1024)
	if not data:
		break
	msg = data.decode()
	print(f'Клиент отправил: {msg}')
	print('Отправка данных клиенту...')
	conn.send(data)


print('Отключение клиента...')

print('Остановка сервера...')
conn.close()

input()