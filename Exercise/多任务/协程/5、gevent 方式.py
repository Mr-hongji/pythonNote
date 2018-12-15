# -*- coding:utf-8 -*-
''''''

'''
Python中还有一个比greenlet更强大的，并且能够自动切换任务的模块 gevent


    gevent是基于协程（greenlet）的网络库，底层的事件轮询基于libev（早期是libevent），
gevent的API概念和Python标准库一致(如事件，队列)。

gevent有一个很有意思的东西-monkey-patch，能够使python标准库中的阻塞操作变成异步，如socket的读写。

'''

import gevent

def A():
    for i in range(5):
        print('A.........')
        print('A,,,,,,,,,')

def B():
    for i in range(5):
        print('B..........')
        print('B,,,,,,,,,,')


gevent.spawn(A)
gevent.spawn(B)



'''

执行结果：

A.........
A,,,,,,,,,
A.........
A,,,,,,,,,
A.........
A,,,,,,,,,
A.........
A,,,,,,,,,
A.........
A,,,,,,,,,
B..........
B,,,,,,,,,,
B..........
B,,,,,,,,,,
B..........
B,,,,,,,,,,
B..........
B,,,,,,,,,,
B..........
B,,,,,,,,,,

代码仍然是顺序执行，因为代码中没有 IO 的耗时操作

'''


'''

下面代码使用 sleep方式 模拟了耗时操作

之前使用的是 time模块的 sleep函数，这段代码中使用的是
 gevent.sleep() gevent自带 sleep 函数

'''

def C():
    for i in range(5):
        gevent.sleep(1)
        print('C..........')

def D():
    for i in range(5):
        gevent.sleep(1)
        print('D..........')


gc = gevent.spawn(C)
gd = gevent.spawn(D)

gc.join()
gd.join()
