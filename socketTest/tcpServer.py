# coding=utf-8

# 参考文档 https://www.cnblogs.com/chengd/articles/7291563.html
# 列模式记录：
#   a.在当前文件右键->Column Selection Mode->用鼠标垂直选择文本
#   b.快捷键：Alt + Shift + Insert
# print('---socket通信---')
'''
1.Socket又称"套接字"，应用程序通常通过"套接字"向网络发出请求或者应答网络请求，使主机间或者一台计算机上的进程间可以通讯。
2.流程记录：
    1 服务器根据地址类型（ipv4,ipv6）、socket类型、协议创建socket
    2 服务器为socket绑定ip地址和端口号
    3 服务器socket监听端口号请求，随时准备接收客户端发来的连接，这时候服务器的socket并没有被打开
    4 客户端创建socket
    5 客户端打开socket，根据服务器ip地址和端口号试图连接服务器socket
    6 服务器socket接收到客户端socket请求，被动打开，开始接收客户端请求，直到客户端返回连接信息。这时候socket进入阻塞状态，
      所谓阻塞即accept()方法一直等到客户端返回连接信息后才返回，开始接收下一个客户端连接请求
    7 客户端连接成功，向服务器发送连接状态信息
    8 服务器accept方法返回，连接成功
    9 客户端向socket写入信息(或服务端向socket写入信息)
    10 服务器读取信息(客户端读取信息)
    11 客户端关闭
    12 服务器端关闭

'''
# netstat -an|find /i "8888"    命令行窗口运行查看

from socket import *
HOST = '0.0.0.0'
PORT = 55555
BUFSIZE = 1024
ADDR=(HOST, PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(2)
print('等待客户端连接...')

tcpCliSock,addr = tcpSerSock.accept()
print('连接来自客户端：',addr)

while True:
    data = tcpCliSock.recv(BUFSIZE)
    if not data:
        tcpCliSock.close()
        break
    rstr = data.decode()
    print(rstr)
    tcpCliSock.sendall(f'***{rstr}'.encode())

tcpSerSock.close()
