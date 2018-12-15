# -*- coding:utf-8 -*-
''''''

import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 服务器 IP
serverAddre = ('192.168.20.125', 8899)

# 创建连接
clientSocket.connect(serverAddre)

# 收取服务器发送的消息
csMsg = clientSocket.recv(1024)

print(str(csMsg))

# 发送消息给服务器
clientSocket.send('client msg')

clientSocket.close()