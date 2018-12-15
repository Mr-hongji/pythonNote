# -*- coding:utf-8 -*-
''''''


'''

    在 Thread 和 Process 中，应当选 Process,因为 Process 更稳定，
而且 Process 可以分不到多台机器上，而，Thread 最多只能分不到同一台
机器的多个 CPU 上。


    
    
manager 模块：

    支持把多进程分布到多台机器上 ，一个服务进程可以作为调度者，
将任务分布到多个进程中，依靠网络通信。

    由于，manager 模块封装的很好，不必了解网络通信的细节，就可以很容易的
编写分布式多进程程序。


比如：
    
    我们已经有一个通过 Queue 通信的多进程程序在同一台机器上运行，
现在，由于处理任务的子进程任务繁重，希望把发送任务的进程和处理任务
的进程分布到两台机器上，怎么用分布式进程实现？
  

'''


import random,time
from multiprocessing.queues import Queue
from multiprocessing.managers import BaseManager

