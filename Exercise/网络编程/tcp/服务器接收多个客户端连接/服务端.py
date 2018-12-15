# -*- coding:utf-8 -*-
''''''

import socket

'''
这段代码实现了服务端可以接受多个客户端连接，但是每次执行：

while True:
    clientSocket, clientAddr = serverSocket.accept()
    
的时候都会重新等待一个客户端连接，之前连接的客户端不能再同服务端互相通信


解决这个问题需要使用多线程的方式

'''

serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

addr = ('192.168.20.125',8859)

serverSocket.bind(addr)

serverSocket.listen(5)

# 不断接收消息
while True:
    clientSocket, clientAddr = serverSocket.accept()

    # 收到客户端连接后，给客户端回一条消息
    clientSocket.send('server socket')

    recvMsg = clientSocket.recv(1024)

    print(recvMsg)

    # 收到 “q”时，退出循环
    if recvMsg == "q":
        break

# 关闭客户端连接
clientSocket.close()

# 关闭服务端连接
serverSocket.close()
