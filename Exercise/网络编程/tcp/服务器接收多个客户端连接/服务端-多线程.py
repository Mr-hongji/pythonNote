# -*- coding:utf-8 -*-
''''''

import socket
import threading


def clientThread(clientSocket):
    global connectNum

    while True:

        try:
            recvMsg = clientSocket.recv(1024)

            print('currentThread : %s,  recvMsg: %s, connectNum '
                  ': %d' %(threading.currentThread().name, recvMsg, connectNum))

            # 收到 “q”时，退出循环
            if recvMsg == "q":
                print('================   connectNum = %d' % connectNum)
                connectNum -= 1
                break

        except:
            pass

    # 关闭客户端连接
    clientSocket.close()



# 当前连接服务器的客户端数
connectNum = -1

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = ('192.168.20.125', 2999)

serverSocket.bind(addr)

serverSocket.listen(5)

# 是否阻塞（默认True），如果设置False，那么accept和recv时一旦无数据，则报错。
serverSocket.setblocking(0)

# 不断接收消息
while True:

    # 只用于测试
    # 如果服务器没有客户端连接，则关闭服务
    print('+++++++++++++   connectNum = %d' % connectNum)
    if connectNum == 0:
        print('------------   ----------')
        break
    try:

        clientSocket, clientAddr = serverSocket.accept()
        # 收到客户端连接后，给客户端回一条消息
        clientSocket.send('server socket')

        socketThread = threading.Thread(target = clientThread, args = (clientSocket,))
        socketThread.start()

        if connectNum < 0:
            connectNum = 1
        else:
            connectNum += 1

    except:
        pass

# 关闭服务端连接
serverSocket.close()
