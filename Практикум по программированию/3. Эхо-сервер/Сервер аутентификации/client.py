import socket
from time import sleep

def c_register():
    print('Регистрация.')
    login = input('Введите логин: ')
    sock.send(login.encode())
    passw = input('Введите пароль: ')
    sock.send(passw.encode())
    data = sock.recv(1024)
    if 'успешно' in data.decode():
        print('Успешная регистрация!')
    else:
        print('Что-то пошло не так.')

def c_login():
    print('Авторизация.')
    login = input('Введите логин: ')
    sock.send(login.encode())
    passw = input('Введите пароль: ')
    sock.send(passw.encode())
    data = sock.recv(1024)
    if 'успешно' in data.decode():
        print('Успешная авторизация!')
    else:
        print('Неверные логин или пароль.')



if __name__ == '__main__':
    sock = socket.socket()
    sock.setblocking(1)

    ip = input('Введите имя хоста (IP-adress): ')
    port = input('Введите порт: ')
    # ip = ''
    # port = 9090

    print('Соединение с сервером...')
    sock.connect((ip, int(port)))

    data = sock.recv(1024)

    if 'регистрация' in data.decode():
        c_register()
    else:
        c_login()
    
    print('Разрыв соединения с сервером...')
    sock.close()

    input()