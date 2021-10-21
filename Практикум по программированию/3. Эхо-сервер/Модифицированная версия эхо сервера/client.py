import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)

ip = input('Введите имя хоста (IP-adress): ')
port = input('Введите порт: ')
# ip = '192.168.1.2'
# port = 9090

print('Соединение с сервером...')
sock.connect((ip, int(port)))

msg = input('Введите сообщение: ')

print('Отправка данных серверу...')
sock.send(msg.encode())

print('Прием данных от сервера...')
data = sock.recv(1024)
print(f'Сервер отправил: {data.decode()}')

print('Разрыв соединения с сервером...')
sock.close()

input()