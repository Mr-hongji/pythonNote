# -*- coding:utf-8 -*-
''''''
'''

Socket
    
    * 通常称为“套接字”，用于描述 IP 地址和端口，
    可以用来实现不同虚拟机或不同计算机之间的通信  
    
    *   本质是编程接口（API）,对 TCP/IP 的封装  
    
    *   套接字连接过程分为三个步骤：
    
        -   服务器监听
        -   客户端请求
        -   连接确认

import socket

socket.socket(AdressFamily = (AF_INET | AF_UNIX), Type = (SOCK_STREAM | SOCK_DGRAM))

    *  socket.socket() 创建一个 socket, 返回该 socket 的描述符
    
    *   该函数带有两个参数：
    
            -   AddressFamily(地址家族)：实际工作中用 AF_INET    
                    1、AF_INET：用于Internet进程间通信
                    2、AF_UNIX：用于同一台机器进程间通信
            
            -   Type: 套接字类型
                    1、SOCK_STREAM：流式套接字，主要用于 TCP 协议
                    2、SOCK_DGRAM：数据报套接字，用于 UDP 协议



'''

'''

UDP: 
    
    *   是一个无连接的传输协议
    
    
缺点：
    
    *  不提供可靠性，只负责把应用程序传个IP层的数据报发送出去，不保证发送成功
            ，传输数据前不用在客户和服务器之间建立连接，并且没有超时重发机制，


优点：
    
    *   传输速度快
   
   
        
一般用于多点通信和实时的数据业务，比如：

    *   语音广播、视频、QQ、TFTP(简单文件传送)、SNMP(简单地网络管理协议)...
    


'''


'''

TCP:
    
    *   可靠连接
    
    *   面向连接的协议，收发数据前必须和对方建立连接


一个TCP连接必须经过三次“对话”才能建立起来：

    -   

'''


'''

----------------------   面试会问   ------------------

TCP 和 UDP 区别：

    1、基于连接 和 无连接
    2、对系统资源要求（TCP较多，UDP少）
    3、UDP程序结构简单
    4、流模式 和 数据报模式
    5、TCP 保证数据的正确性，UDP 可能丢包
    6、TCP 保证数据顺序，UDP 不保证

'''