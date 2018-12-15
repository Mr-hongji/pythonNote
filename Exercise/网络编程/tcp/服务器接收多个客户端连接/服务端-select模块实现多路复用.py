# -*- coding:utf-8 -*-
''''''

'''

select介绍

    * 在python中，select函数是一个对底层操作系统的直接访问的接口。
    * 它用来监控sockets、files和pipes，等待IO完成（Waiting for I/O completion）。
    * 当有可读、可写或是异常事件产生时，select可以很容易的监控到。

select.select（rlist, wlist, xlist[, timeout]） 

    * 传递三个参数:

        - rlist 为输入而观察的文件对象列表
        - wlist 为输出而观察的文件对象列表
        - xlist 观察错误异常的文件列表
        - timeout 可选参数，表示超时秒数。
        - 其返回3个tuple，每个tuple都是一个准备好的对象列表，它和前边的参数是一样的顺序。



'''


'''

示例：

监听客户端连接，当有客户端输入时，接收输入并打印，同时把该客户端添加到输出监听，
接收到输出时，向客户端输出信息

'''

import socket
import select

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = ('192.168.20.125', 2999)

serverSocket.bind(addr)

serverSocket.listen(5)

inputs = [serverSocket] # 初始化将服务端加入监听列表
outputs = []
errputs = []


while True:

    # 1、select函数阻塞进程，直到inputs中的套接字被触发（在此例中，套接字接收到客户端发来的握手信号，
    # 从而变得可读，满足select函数的“可读”条件），rs返回被触发的套接字（服务器套接字）；
    # 4、select再次阻塞进程，同时监听服务器套接字和获得的客户端套接字；
    # 开始 select 监听,inputs 中的服务端server进行监听
    # 当客户端 A 连接服务端 则 readlist = [A]
    # 又有一个客户端 B 连接服务端 则 readlist = [A， B]
    # 客户端 A 在 recv 的时候，则  writeList = [A]
    readlist, writeList, errorList = select.select(inputs, outputs, errputs)

    for conn in readlist:  #2、如果是服务器套接字被触发（监听到有客户端连接服务器）
        if conn is serverSocket:
            clientConn, clientAddr = serverSocket.accept()

            # 将客户端对象也加入到监听的列表中, 当客户端发送消息时 select 将触发
            inputs.append(clientConn)
        else: # 当客户端发送数据时，客户端套接字被触发，rs返回客户端套接字，然后进行下一步处理。
            try:
                recvMsg = conn.recv(1024)

                print('recvMsg = ' + recvMsg)

                if conn not in outputs:
                    # 把当前客户端Socket 放到outputs中，让select 进行监听
                    # 当outputs 中的 客户端在等待接收时，会触发select
                    outputs.append(conn)
            except:
                inputs.remove(conn)
                if conn in outputs:
                    outputs.remove(conn)


    for cserver in writeList:
        try:
            cserver.send('123')
        except:
            print('数据发送失败...')
        finally:
            outputs.remove(conn)
