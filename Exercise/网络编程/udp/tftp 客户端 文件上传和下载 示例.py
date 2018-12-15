# -*- coding:utf-8 -*-
''''''

'''
此项目搭建主要使用的技术是Python的sockt（UDP协议）+ TFTP协议

使用工具:
    
    Tftpd32-4.52-setup 

TFTP（Trivial File Transfer Protocol)：简单文件传输协议:

    * TFTP是TCP/IP协议族中的一个用来在客户端与服务器之间进行简单文件传输的协议，传输不复杂、开销不大的文件。
    
    * TFTP服务器默认监听69号端口
    
            - 当客户端发送“下载”请求（即读请求）时，需要向服务器的69端口发送服务器若批准此请求,
        则使使用一个个新的、临时的端口进口数据传输。
        
            - 为了标记数据已经发送完毕，所以规定，当客户端接收到的数据口于516（2字节操作码+2个字节的序号+512字节数据）
        时，就意味着服务器发送完毕了

    * TFTP数据包的格式如当前目录下（tftp 数据包格式.png）
    
    * 特点
    
        - 简单、占用资源少、基于UDP实现、端口号为69、适合在局域网内传输小文件。

'''


'''

struct模块:

    * 最近一段时间在看有关Python相关的知识，特别是其中关于网络通信的内容。在大部分的书本示例中，
    客户端和服务器端通信的内容都是文本信息，例如“hello world！”之类的信息。但是在实际应用中，
    我们看到的大部分数据是二进制数据，如“0x12345678”。所以这时候，就需要使用到Python中的struct来处理一下了。

    * 用python处理二进制数据，比如，存取文件，socket操作时.这时候，可以使用python的struct模块来完成.
   可以用 struct来处理c语言中的结构体.

    * struct模块中最重要的三个函数是pack(), unpack(), calcsize()

        - pack(fmt, v1, v2, ...)     
            按照给定的格式(fmt)，把数据封装成字符串(实际上是类似于c结构体的字节流)

        - unpack(fmt, string)       
            按照给定的格式(fmt)解析字节流string，返回解析出来的tuple

        - calcsize(fmt)                 
            计算给定的格式(fmt)占用多少字节的内存

'''

import socket,struct

addre = ('192.168.20.125', 69)

def downloadFile():
    tftpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 打包请求的数据格式
    sendMsg = struct.pack('!H6sb5sb', 1, b'tt.png', 0, b'octet', 0)

    tftpSocket.sendto(sendMsg, addre)

    f = None

    while True:
        # 收数据
        revData = tftpSocket.recvfrom(1024)

        print revData

        # 解包返回的数据中的 操作码 和 编号
        code = struct.unpack('!HH', revData[0][:4])

        oc = code[0] # 操作码（包类型）

        # 根据包类型进行不同处理
        if oc == 5: # 操作码=5，返回的是错误信息
            print("错误信息：" + revData[0][4:])
            break
        elif oc == 3: # 正常数据
            oc_No = code[1]  # 编码 （包序号）
            if oc_No == 1: # 收到第一个数据包
                f = open('d:/tt.png', 'wb')
                f.write(revData[0][4:])
            else: # 后续数据包
                f.write(revData[0][4:]) # 收到的数据默认长度是512个字节

            # 收到服务端的数据之后，给服务端发送确认消息
            # 确认信息不要发给原来的服务器，revData[1] 中存放的是服务器给你发的数据的新地址
            # 服务器只是接受请求的，服务器可以接受多个客户端连接
            # 接到客户端的请求后，会新建一个 socket ，然后用这个新的socket跟这个客户端通信
            ackMsg = struct.pack('!HH', 4, oc_No)
            tftpSocket.sendto(ackMsg,revData[1])

            # 数据包中的数据的长度如果小于512，就默认文件已经接收完毕
            if len(revData[0][4:]) < 512:
                f.close()
                break

    # print code
    tftpSocket.close()



def uploadFile():
    upfSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 连接服务器信息  告诉服务器 客户端要上传文件 pp.png
    # 这是客户端请求上传操作 所以操作码是 2
    upMsg = struct.pack('!H6sb5sb',2, b'pp.png', 0, b'octet', 0)

    upfSocket.sendto(upMsg, addre) # 开始连接服务

    fileContent = None
    i = 0

    while True:
        serverData = upfSocket.recvfrom(1024) # 接收服务端的 ACK确认信息
        print serverData

        serverCode = struct.unpack('!HH',serverData[0][:4]) # 解包 操作码

        print serverCode

        if serverCode[0] == 5: # 操作码等于5，是服务端返回的错误信息
            print('错误码：' + serverCode[0] +  ' 错误信息：' + serverData[0][4:])
            break
        elif serverCode[0] == 4: # ACK 确认信息
            f = open('d:/pp.png', 'rb') # 打开文件
            f.seek(i*512,0) # 设置读取文件开始的索引位置
            i += 1
            fileContent = f.read(512) # 读取512字节的数据
            f.close()

            # 打包从文件中读取的512 字节的数据，发送给服务器
            # 因为这个是向服务端上传数据，所以，这个是数据包，所以，操作码是 3
            upDataPack = struct.pack('!HH%ss' % str(len(fileContent)), 3, serverCode[1] + 1, fileContent)
            upfSocket.sendto(upDataPack, serverData[1])

            # 从文件中读取到的数据小于512字节时，判断为数据上传结束
            if len(fileContent) < 512:
                break




if __name__ =='__main__':
    uploadFile()
    downloadFile()