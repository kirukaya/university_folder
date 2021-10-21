import socket
from time import sleep
import re

def s_send(sock, data, token = ''):
    data = bytearray(f'{len(data)}$@$~{data}$token={token}$'.encode())
    sock.send(data)

def s_recv(sock):
    data = sock.recv(1024).decode()
    indx = data.find('$@$~')
    pswd = data.rfind('$$$~')
    answ = data.rfind('@$$~')
    atkn = re.search('\$token=(.{32,32})\$', data)

    print('Recieved message length - {}'.format(data[:indx]))

    if pswd>-1:
        return data[indx+4:pswd], 1

    elif answ>-1:
        return data[indx+4:answ], 2

    elif atkn:
        indx2 = atkn.start()

        return (data[indx+4:indx2], atkn[1]), 3
    else:
        return data[indx+4:], 0



def main():
    while True:
        msg = input('msg: ')
        sock.s_send(msg)
        data = sock.s_recv()[0]
        print('server: '+data)
    sock.close()


if __name__ == '__main__':
    socket.socket.s_send = s_send
    socket.socket.s_recv = s_recv

    sock = socket.socket()
    sock.setblocking(1)

    ip = input('Введите IP-адресс: ')
    port = input('Введите порт: ')

    # ip = ''
    # port = 9090

    print('Соединение с сервером...')
    sock.connect((ip, int(port)))

    main()