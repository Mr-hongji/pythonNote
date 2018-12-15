# -*- coding:utf-8 -*-
''''''
'''

UDP 发送数据


 使用网络助手运行调试下面代码效果!

'''

import socket

# 1、创建套接字

udpSocket1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2、准备接收方的地址

sendAddress = ('127.0.0.1',8080)

# 3、发送数据

udpSocket1.sendto('UDP Test', sendAddress)

# 4、接收数据
# 1024 表示本次接收的最大字节数

recMsg = udpSocket1.recvfrom(1024)

print('udpSocket1... %s' % str(recMsg))

udpSocket1.close()



'''

绑定地址和端口

    * 如果一个网络程序，不绑定端口，则系统会随机分配，这时候其他程序就不能知道
    这个程序的端口，所以此程序就不会收到消息

'''

udpSocket2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定本地的相关信息
# Ip 和端口号，Ip  一般不用写，表示本机的任何一个 Ip

address = ('',1234)

udpSocket2.bind(address)

msg = udpSocket2.recvfrom(1024)

print('udpSocket2... %s' %str(msg))

udpSocket2.close()



'''

echo服务器


'''

udpSocket3 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

udpSocket3.bind(address)

while True:

    # 等待接收对方发送的数据

    msg = udpSocket3.recvfrom(1024)

    # 将接收的数据再发送给对方

    udpSocket3.sendto(msg[0], msg[1])

    # 打印收到的信息

    print('udpSocket3... %s' % str(msg))


udpSocket3.close()
