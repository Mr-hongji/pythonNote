# -*- coding:utf-8 -*-
''''''
import socket

# 创建socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = ('192.168.20.125',8899)

# 绑定 IP
serverSocket.bind(addr)

# 设置监听
serverSocket.listen(5)

# 等待客户端连接
# 调用accept()函数等待连接的到来，默认情况下accept()函数是阻塞的，即程序在连接到来之前会处于挂起状态
# 接收到一个连接，accept()函数就会返回一个单独的客户端套接字用于后续的通信
clientSocket, clientAddr = serverSocket.accept()

print('收到客户端：%s' %clientAddr[0])

clientSocket.send('server msg')

recvMsg = clientSocket.recv(1024)

print(str(recvMsg))

clientSocket.close() # 关闭客户端套接字
serverSocket.close() # 关闭服务器