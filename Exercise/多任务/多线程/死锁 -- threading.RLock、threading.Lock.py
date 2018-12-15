# -*- coding:utf-8 -*-

''''''

'''

Lock & RLock

    *   Lock:

        -   Lock 对象的状态可以为 locked 和 unlocked
    
        -   使用acquire()设置为locked状态
        
        -   使用release()设置为unlocked状态
        
        -   如果当前的状态为 unlocked，则 acquire() 会将状态改为 locked 然后立即返回
        
        -   当状态为 locked 的时候，acquire() 将被阻塞直到另一个线程中调用 release() 
        来将状态改为 unlocked, 然后 acquire() 才可以再次将状态置为 locked
        
        -   Lock.acquire(blocking=True)
        
                >   blocking：参数表示是否阻塞当前线程等待
                
                    ::  如果成功地获得lock，则acquire()函数返回True，否则返回False，
                
                        
    *   RLock：可重入锁
    
            -   支持在同一线程中多次请求同一资源
    
            -   RLock中除了状态 locked 和 unlocked 外还记录了当前 lock 的 owner 和递归层数，
                使得 RLock 可以被同一个线程多次 acquire()，直到一个线程所有的 acquire 
                都被 release，其他的线程才能获得资源。
            
                

死锁:
    
    *   迭代死锁
    
    *   互相调用死锁

'''



import threading,time



'''
    
    迭代死锁：
        
        下面示例，在run函数的if判断中第一次请求资源，请求后还未 release ，
        再次acquire，最终无法释放，造成死锁。这里例子中通过将print
        下面的两行注释掉就可以正常执行了 ，除此之外也可以通过可重入锁解决，
        后面会提到。

'''

import threading
import time

num = 0

mutex = threading.Lock()

class MyThread11(threading.Thread):
    def run(self):
       global num
       for i in range(2):
           if mutex.acquire():
                num = num + 1
                msg = self.name+' set num to '+str(num)
                mutex.acquire()
                mutex.release()
                mutex.release()
                print msg

def test1():
    for i in range(5):
        t = MyThread11()
        t.start()





'''

    互相调用死锁：
    
        两个函数中都会调用相同的资源，互相等待对方结束的情况。
        如果两个线程分别占有一部分资源并且同时等待对方的资源，就会造成死锁。

'''



resA = 0
resB = 0

mutexA = threading.Lock()
mutexB = threading.Lock()

class MyThread(threading.Thread):
    def do1(self):
        global resA, resB
        if mutexA.acquire():
            msg = self.name + ' got resA'
            print msg
            if mutexB.acquire(1):
                msg = self.name + ' got resB'
                print msg
                mutexB.release()
            mutexA.release()

    def do2(self):
        global resA, resB
        if mutexB.acquire():
            msg = self.name + ' got resB'
            print msg
            if mutexA.acquire(1):
                msg = self.name + ' got resA'
                print msg
                mutexA.release()
            mutexB.release()

    def run(self):
        self.do1()
        self.do2()


def test2():
  for i in range(5):
    t = MyThread()
    t.start()



'''

    使用 RLock
    
'''


num = 0

class MyThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)
        if mutex.acquire(1):
            num = num + 1
            msg = self.name + ' set num to ' + str(num)
            print msg
            mutex.acquire()
            mutex.release()
            mutex.release()

mutex = threading.RLock()

def test3():
    for i in range(5):
        t = MyThread()
        t.start()




if __name__ == '__main__':

    test1() # 迭代死锁

    # test2() # 互相调用死锁示例

    # test3() # threading.RLock测试