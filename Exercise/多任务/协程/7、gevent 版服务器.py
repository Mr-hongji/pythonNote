# -*- coding:utf-8 -*-
''''''

import gevent


from gevent import monkey,socket

# 先打补丁 （pach）
monkey.patch_all()

def func(conn):
    try:
        msg = conn.recv(1024)
        print(str(msg))
        conn.close()
    except:
        print('error!')

# gevent 中的 socket 没有参数：socket.AF_INET, socket.SOCK_STREAM
serverSocket = socket.socket()

addr = ('192.168.20.125',9988)

serverSocket.bind(addr)

serverSocket.listen(5)

while True:
    clientSocket, clientAdd = serverSocket.accept()
    print('客户端地址：%s, 端口：%d' %(clientAdd[0],clientAdd[1]))

    # 生成一个协程 处理连接的客户端数据
    gevent.spawn(func, clientSocket)