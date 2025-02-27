import socket
from threading import Thread
import os
import time

N = 2**16 - 1 # 65535 портов

portsProgress = [0 for _ in range(N)]
openports = []

def checkPort(i):
    for port in range(66*i,66*(i+1)): #1,66
        if 0<=port<=N:
            portsProgress[port] = 1
            sock = socket.socket()
            try:
                #print(port)
                sock.connect(('127.0.0.1', port))
                print("Порт", i, "открыт")
                openports.append(port)
            except:
                continue
            finally:
                sock.close()

threads = []
for i in range(1000):
    threads.append(Thread(target=checkPort, args=[i]))

for i in threads:
    i.start()

while True:
    os.system('cls')
    prog = (portsProgress.count(1)/N)*100
    print(f'{prog: .2f}%', end = '')
    print(' ['+'▓'*(int(prog)//2)+' '*(50-(int(prog)//2))+']')
    time.sleep(1)
    if prog==100.00:
        os.system('cls')
        print('Completed! ['+50*'▓'+']')
        print(f'Open ports: {openports}')
        break
input()