import socket
import random 

def print_log(msg, clr = False):
	func = {True: 'w', False: 'a'} # запись и дозапись соответственно
	with open('logs.txt', func[clr], encoding='utf8') as f:
		print(msg, file = f)
	
sock = socket.socket()
print_log('Запуск сервера...', clr = True)

port = 9090
ready = False
while not ready:
	try:
		sock.bind(('', port))
		ready = True
		print(f'{port}')
	except:
		pport = port
		port = random.randint(1000, 9999)
print_log(f'Прослушивание порта {port}...')
sock.listen(0)

while True:
	conn, addr = sock.accept()
	print_log(f'Подключение клиента {addr}')

	print_log('Прием данных от клиента...')
	while True:
		data = conn.recv(1024)
		if not data:
			break
		msg = data.decode()
		print_log(f'Клиент отправил: {msg}')
		print_log('Отправка данных клиенту...')
		conn.send(data)
	print_log('Отключение клиента...')

print_log('Остановка сервера...')
conn.close()