import socket
from time import sleep
from threading import Thread
import tkinter as tk
from tkinter import * 
from tkinter import ttk   
import time
import sys

def c_register(sock):
    global authorized
    print('Регистрация.')
    login = input('Введите логин: ')
    sock.send(login.encode())
    passw = input('Введите пароль: ')
    sock.send(passw.encode())
    data = sock.recv(1024)
    if 'успешно' in data.decode():
        print('Успешная регистрация!')
        authorized = True
    else:
        print('Что-то пошло не так.')

def c_login(sock):
    global authorized
    print('Авторизация.')
    login = input('Введите логин: ')
    sock.send(login.encode())
    passw = input('Введите пароль: ')
    sock.send(passw.encode())
    data = sock.recv(1024)
    if 'успешно' in data.decode():
        print('Успешная авторизация!')
        authorized = True
    else:
        print('Неверные логин или пароль.')

def socketFunc():
    global authorized, sock, chats, allchatchange, authorized, end
    # try:
    sock = socket.socket()
    sock.setblocking(1)
    chats = {}
    # ip = input('Введите имя хоста (IP-adress): ')
    # port = input('Введите порт: ')
    ip = '192.168.1.2'
    port = 9090
    print('Соединение с сервером...')
    sock.connect((ip, int(port)))
    data = sock.recv(1024)
    if 'регистрация' in data.decode():
        c_register(sock)
    else:
        c_login(sock)
    if authorized:
        print('Открылось графическое окно чата, перейдите в него.')
        while True:
            data = sock.recv(1024)
            if 'новый пользователь' in data.decode():
                pass
            else:
                chats = eval(data.decode())
                allchatchange = True
                #print(chats)
    else:
        print('Попробуйте снова')
        end = True

    # except ConnectionRefusedError:
    #     print('Сервер неактивен.')
    # except:
    #     print('Разрыв соединения с сервером...')
    #     sock.close()

def editChat(*box):
    global allchatchange
    allchatchange = False
    c = 0
    while True:
        #curval = box[0].get("1.0", END)
        if 'allchat' in chats.keys() and allchatchange:
            line = f"{chats['allchat'][c][0][0]}: {chats['allchat'][c][1]}\n"
            box[0].insert(100.0, line)
            allchatchange = False
            c+=1
        time.sleep(0.1)

def checkMsgBox(*msgbox):
    while True:
        curval = msgbox[0].get("1.0",END)
        if curval.count('\n') > 1:
            sock.send(f'allchat{curval}'.encode())
            msgbox[0].delete(0.0, 'end')
        time.sleep(0.1)

class ChatTab():
    def __init__(self):
        self.tab = Frame(tabControl, bg = 'black', width = wdth)
        tabControl.add(self.tab, text = 'Monitors')
        #tabControl.pack(expand=50, fill='both') 

def app():
    global tabControl, authorized, end
    end = False
    Thread(target = socketFunc, daemon = True).start()
    authorized = False
    while not authorized:
        if end:
            sys.exit()
        time.sleep(1)
    root = Tk() 
    root.title("client.py")  
    root.configure(background='black')
    wdth, hght = 300, 400
    root.geometry(f'{wdth}x{hght}')
    root.resizable(width=False, height=False)

    tabControl = ttk.Notebook()

    alltab = Frame(tabControl, bg = 'black', width = wdth)
    allbox = Text(alltab, width = wdth, height = 13, font='TkDefaultFont 16')   
    msgallbox  = Text(alltab, width = wdth, font='TkDefaultFont 16')                          
    allbox.pack(side=TOP)
    msgallbox.pack(side=BOTTOM)
    Thread(target=checkMsgBox, daemon = True, args = [msgallbox]).start()
    Thread(target=editChat, daemon = True, args = [allbox]).start()
    
    tabControl.add(alltab, text = 'All Chat')
    
    tabControl.pack(expand=50, fill='both')

    root.mainloop()

if __name__ == '__main__': 
    app()