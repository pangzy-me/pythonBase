# coding=utf-8

from socket import *
HOST = '127.0.0.1'
PORT = 55556
BUFSIZE = 1024
ADDR=(HOST, PORT)
2
tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('客户端输入>> ')
    if data == '':
        break
    tcpCliSock.send(data.encode())

    data = tcpCliSock.recv(BUFSIZE)
    if not data:
        break
    print(data.decode())

tcpCliSock.close()
