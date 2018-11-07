# coding=utf-8
import threading,socket

HOST = ''
PORT = 55556
BUFSIZE = 1024
ADDR = (HOST,PORT)

# 每产生一个新线程，负责一个客户端与服务端进行通信
def new_client_thread(clientsocket,addr):
    while True:
        data = clientsocket.recv(BUFSIZE)
        if not data:
            print('%s 关闭了连接。'% addr)
            break
        rstr = data.decode()
        print(f'客户端地址为{addr}| 请求内容为:{rstr}')
        clientsocket.send(data)
    clientsocket.close()

servsocket = socket.socket()
servsocket.bind(ADDR)
servsocket.listen(5)

while True:
    clientsocket,addr = servsocket.accept()
    addr = str(addr)
    print(f'从{addr}过来的客户端连接>>>')
    clientThread = threading.Thread(target=new_client_thread,args=(clientsocket,addr))
    clientThread.start()

