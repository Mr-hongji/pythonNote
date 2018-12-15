# -*- coding:utf-8 -*-
''''''


'''
Lock

    *   优点：
    
        -   确保了某段关键代码只能由一个线程从头到尾完整地执行
        
    *   缺点：
    
        -   首先，阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了
        
        -   其次，由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁，
                导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止。

'''




'''

多线程中，所有变量被所有线程共享，所以，任何一个变量都可以被任何一个线程修改，
因此，线程之间共享数据最大的危险在于多个线程同时修改一个变量，容易把内容改乱

如下示例：

'''

import threading,time

balance = 0

def change_Balance(n):
    global balance
    balance = balance + n
    balance = balance - n
    print(threading.currentThread().name)

def run_t(n):
    for i in range(1000):
        change_Balance(n)

if __name__ == "__main__":
    t1 = threading.Thread(target = run_t, args = (5,))
    t2 = threading.Thread(target=run_t, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('balance = %s' % balance)



'''

运行结果：
    
    第一次：balance = 5
    第二次：balance = 0
    第三次：balance = -45
    第四次：balance = -40
    第五次：balance = 0
    
每一次的运行结果都是不一定的
    
    
上面代码中，定义了一个共享变量，初始值是0，并启动两个线程进行先加后减，
理论上最后结果应该是0，但是由于线程的调度是由操作系统决定，当t1,t2交替执行时，
只有循环次数足够多，balance的结果就不一定是0了

'''


'''

在高级语言中，一条语句在CPU中执行时是若干条语句，
即使一个简单的计算：balance = balance + n 也分两步：

    1、计算 balance + n , 存入临时变量
    2、将临时变量的值赋值给 balance

如：

    x = balance + n
    balance = x
    
    
由于 x 是局部变量，两个线程都有自己的 x, 当代码正常执行时如下代码：
 
 
    # 初始值
    balance = 0
    
    # t1:
    x1 = balance + 5 # x1 = 0 + 5 = 5
    balance = x1     # balance = 5
    x1 = balance - 5 # x1 = 5 - 5 = 0
    balance = x1     # balance = 0
    
    # t2:
    x2 = balance + 8 # x2 = 0 + 8 = 8
    balance = x2     # balance = 8
    x2 = balance - 8 # x2 = 8 - 8 = 0
    balance = x2     # balance = 0
    
    # 结果 balance = 0
 
'''



'''

但是t1和t2是交替运行的，如果操作系统以下面的顺序执行t1、t2：

    # 初始值
    balance = 0
    
    # t1
    x1 = balance + 5  # x1 = 0 + 5 = 5
    
    # t2
    x2 = balance + 8  # x2 = 0 + 8 = 8
    balance = x2      # balance = 8
    
    # t1
    balance = x1      # balance = 5
    x1 = balance - 5  # x1 = 5 - 5 = 0
    balance = x1      # balance = 0
    
    # t2
    x2 = balance - 8  # x2 = 0 - 8 = -8
    balance = x2   # balance = -8
    
    # 结果 balance = -8

'''



'''

究其原因，是因为修改balance需要多条语句，而执行这几条语句时，线程可能中断，
从而导致多个线程把同一个对象的内容改乱了。

两个线程同时一存一取，就可能导致数据不对，所以，
我们必须确保一个线程在修改balance的时候，别的线程一定不能改。

如果我们要确保balance计算正确，就要给change_Balance()上一把锁，当某个线程开始执行change_Balance()时，
我们说，该线程因为获得了锁，因此其他线程不能同时执行change_Balance()，只能等待，直到锁被释放后，获得该锁以后才能改。
由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，所以，不会造成修改的冲突

'''


'''
    lock = threading.Lock()——创建锁 lock
        
    lock.acquire()——获取锁

    lock.release()——释放锁

'''

lock = threading.Lock()

def run_t1(n):
    for i in range(10):
        # 先要获取锁
        lock.acquire()
        try:
            # 放心地改吧
            change_Balance(n)
        finally:
            # 改完了一定要释放锁
            lock.release()


if __name__ == '__main__':
    rt1 = threading.Thread(target=run_t1,args=(5,))
    rt2 = threading.Thread(target=run_t1, args=(8,))
    rt1.start()
    rt2.start()
    rt1.join()
    rt2.join()
    print('balance111 = %s' % balance)



'''

代码解释：

    当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，然后继续执行代码，
    其他线程就继续等待直到获得锁为止。

    获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。
    所以我们用try...finally来确保锁一定会被释放。

'''



'''

小结：
    
    在Python中，可以使用多线程，但不要指望能有效利用多核。如果一定要通过多线程利用多核，
    那只能通过C扩展来实现，不过这样就失去了Python简单易用的特点。

    不过，也不用过于担心，Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。
    多个Python进程有各自独立的GIL锁，互不影响。


    多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。

    Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。
    多线程的并发在Python中就是一个美丽的梦。

'''