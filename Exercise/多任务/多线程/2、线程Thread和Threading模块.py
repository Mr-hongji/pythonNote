# -*- coding:utf-8 -*-
''''''

'''

Python中提供了了thread和threading两个模块

    *   thread是低级模块，threading是高级模块，并对thread进行了封装
    
    *   绝大多数情况下只需使用threading   
    
    *  len(threading.enumerate()) 获取当前线程
    

避免使用thread模块的原因：

    * thread 模块中有一些属性会和 threading模块有冲突
    
    * threading模块提供的同步原语要更多
        
        - threading 模块提供的线程同步原语包括：Lock、RLock、Condition、Event、Semaphore等对象。
    
    * thread 不支持守护线程，对进程何时退出没有控制。
        
        -  当主线程结束时，所有子线程也都会强制结束，
            不管他们是否仍在工作，并且不会发出警告或者进程适当清理
    
'''

import threading, time

def loop():
    print('thread %s is running...' % threading.currentThread().name)
    n = 0
    while n < 5:
        print('thread %s --> %s' % (threading.currentThread().name, n))
        time.sleep(2)
        n += 1

    print('thread %s ended...' % threading.currentThread().name)


if __name__ == '__main__':


    print 'thread %s is running...' % threading.currentThread().name
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()
    print('thread %s ended...' % threading.currentThread().name)


'''

执行结果：

    thread MainThread is running...
    thread LoopThread is running...
    thread LoopThread >>> 1
    thread LoopThread >>> 2
    thread LoopThread >>> 3
    thread LoopThread >>> 4
    thread LoopThread >>> 5
    thread LoopThread ended.
    thread MainThread ended.



代码解释：

    *   任何一个进程默认都会启动一个线程，称为主线程，主线程又可以启动新线程
    
    *   threading.currentThread() 返回当前线程的实例

    *   threading.currentThread().name 获取当前线程的名称
    
    *   t = threading.Thread(target=loop, name='LoopThread') 
        
        -   name是子线程名称，用来打印显示，没有其他意义，如果不传,默认为Thread1,Thread2...
    
'''


