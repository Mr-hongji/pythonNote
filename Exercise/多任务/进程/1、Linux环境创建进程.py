# -*- coding:utf-8 -*-

''''''

'''

Linu环境下创建新进程：

    os模块中fork()函数:

        *   使用os模块中fork()函数可以创建新进程

        *   fork()调用一次返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），
        然后，分别在父进程和子进程内返回

        *   子进程永远返回0，父进程返回子进程的ID

        *   python程序一开始运行的时候，系统会生成一个进程(父进程)，在程序代码中调用fork()函数创建一个新进程
        ，新进程会是原来进程的子进程，原进程称为父进程，参考：http://www.01happy.com/python-fork-create-process/

        *   使用fork()创建子进程后，系统会先给子进程分配资源（如：存储数据和代码的空间），
        然后把父进程的所有资源都复制到子进程中，只有少数值与父进程的值不同（相当于克隆了一个自己，
        然后作为子进程）。

        *   创建进程成功后，系统会出现两个几乎完全相同的两个进程，这两个进程执行没有固定的先后顺序，
        那个进程先执行要看系统的调度算法


    getpid() getppid():

        * 每个进程都有一个标识符（pid：progress ID）

        *   getpid()获取子进程pid

        *   子进程使用getppid()获取父进程pid


进程有独立的内存空间，不能共享全局变量：

    *   如下面代码中的 num变量

    *   子进程中输出的结果是11，父进程中输出的结果是依然是10

    *   子进程中对num做了修改，并不影响父进程中的num


'''


import os
import time

#创建子进程之前声明的变量
num = 10

fid = os.fork()

if fid < 0:
    info = "进程创建失败... fid = %f" % fid
    print(info)

elif fid == 0:
    time.sleep(3) # 休眠3秒
    num = num + 1
    info = "子进程... fid = %d， pid = %d, ppid = %d " % (fid,os.getpid(),os.getppid(), num)
    print(info)

else:
    time.sleep(5) # 休眠5秒
    info = "父进程... fid = %d， pid = %d, ppid = %d, num = %d" % (fid, os.getpid(), os.getppid(),num)
    print(info)