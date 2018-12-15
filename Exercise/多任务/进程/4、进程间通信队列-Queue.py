# -*- coding:utf-8 -*-
''''''

'''

进程间通信

    *   系统提供了很多机制实现进程间通信，
    
        -   multiprocessing模块提供了Queue、Pipes等多种方式进行交换数据
        


Pool 和 Pocess 使用 Queue 的方式：

    *   Queue队列
            
            1、设有内部锁，保证数据先进先出

    *   导入 Queue
    
        1、from multiprocessing import Queue
        
        2、 q = Queue()
        
        
    *   Pool 需要使用 Manager 类来创建 Queue
        
        1、 from multiprocessing import Manager
        
        2、 q = Manager().Queue()

'''



'''

    Process之间用队列（Queue）进行通信：

'''

from multiprocessing import Process,Queue
import os,time

def write_process_run(q,type):
    for value in ['A', 'B', 'C']:
        print 'Put %s to queue. type = %s' % (value,type)
        q.put(value)
        time.sleep(2)

def read_process_run(q,type):
    while True:
        value = q.get(True)
        print 'Get %s from queue. type = %s' % (value,type)
        if value == 'C':
            break

if __name__ == '__main__':
    print('parent process %s start' % os.getpid())
    q = Queue() # 父进程创建Queue，并传给子进程
    pw = Process(target=write_process_run, args=(q,'process_write',))
    pr = Process(target=read_process_run, args=(q,'process_read',))
    pw.start() # 启动子进程写入
    pr.start()  # 启动子进程读取
    pw.join()   # 等待写入进程结束
    pr.terminate()  # 由于用来读取的线程是死循环，所以强行停止
    print('parent process %s ended...' % os.getpid())



'''

    进程池（Pool），使用队列（Queue）进行进程间通信：

'''


from multiprocessing import Pool
from multiprocessing import Manager

if __name__ == '__main__':

    q = Manager().Queue()

    pool = Pool(3)
    pool.apply_async(write_process_run,args=(q,'pool_write',))
    pool.apply_async(read_process_run, args=(q, 'pool_read',))
    pool.close()
    pool.join()
    pool.terminate()
    print('进程池运行结束...')