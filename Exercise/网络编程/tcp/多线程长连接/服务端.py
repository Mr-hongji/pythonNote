# -*- coding:utf-8 -*-
''''''

import socket

serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

addr = ('192.168.20.125',8894)

serverSocket.bind(addr)

serverSocket.listen(5)

clientSocket,clientAddr = serverSocket.accept()

print('收到客户端 %s' % clientAddr[0] + ' 连接')

# s收到客户端连接后，给客户端回一条消息
clientSocket.send('server socket')

# 不端接收消息
while True:

    recvMsg = clientSocket.recv(1024)

    print(recvMsg)

    # 收到 “q”时，退出循环
    if recvMsg == "q":
        break

# 关闭客户端连接
clientSocket.close()

# 关闭服务端连接
serverSocket.close()
