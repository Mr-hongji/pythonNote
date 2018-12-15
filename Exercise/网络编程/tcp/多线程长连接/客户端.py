# -*- coding:utf-8 -*-
''''''

import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = ('192.168.20.125',8894)

# 连接服务器
clientSocket.connect(addr)

# 等待接收消息
recvMsg = clientSocket.recv(1024)

print(recvMsg)

# 给服务端回消息
clientSocket.sendto('client socket - 1', addr)

while True:
    inputMsg = raw_input("Input Msg:")
    inputMsg = str(inputMsg)
    clientSocket.sendto(inputMsg, addr)

    if inputMsg == 'q':
        break

clientSocket.close()