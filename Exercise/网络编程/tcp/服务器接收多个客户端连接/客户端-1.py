# -*- coding:utf-8 -*-
''''''

import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = ('192.168.20.125',2999)

clientSocket.connect(addr)

clientSocket.sendto('client socket - 1', addr)

recvMsg = clientSocket.recv(1024)

print(recvMsg)

while True:
    inputMsg = raw_input("Input Msg:")
    inputMsg = str(inputMsg)
    clientSocket.sendto(inputMsg, addr)

    recvMsg = clientSocket.recv(1024)

    print(recvMsg)

    if inputMsg == 'q':
        break

clientSocket.close()