import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)

print('Соединение с сервером...')
sock.connect(('192.168.1.2', 9090))

msg = input()

print('Отправка данных серверу...')
sock.send(msg.encode())

print('Прием данных от сервера...')
data = sock.recv(1024)
print(f'Сервер отправил: {data.decode()}')

print('Разрыв соединения с сервером...')
sock.close()

input()