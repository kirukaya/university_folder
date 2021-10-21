import socket
import re

def s_send(sock, data, service_data=''):
    data = bytearray(f'{len(data)}$@$~{data}{service_data}'.encode())
    sock.send(data)

def s_recv(sock):
    data = sock.recv(1024).decode()
    indx = data.find('$@$~')
    atkn = re.search('\$token=(.{32,32})\$', data)
    if atkn:
        data = data[:atkn.start()]
        atkn = atkn[1]
    else:
        atkn = ''
    print('Recieved message length - {}'.format(data[:indx]))
    return data[indx+4:], atkn

def main():
	try:
		while True:
			conn, addr = sock.accept()
			print(f'Подключение клиента {addr}')
			while True:
				data = conn.s_recv()
				print('client: '+data[0][:data[0].find('$token')])
				msg = input('msg: ')
				conn.s_send(msg)
			print('Отключение клиента...')
	except:
		print('Остановка сервера...')
		conn.close()


if __name__ == '__main__':
	socket.socket.s_send = s_send
	socket.socket.s_recv = s_recv

	sock = socket.socket()
	print('Запуск сервера...')

	port = 9090
	sock.bind(('', port))
	print(f'Прослушивание порта {port}...')
	sock.listen(0)

	main()