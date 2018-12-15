# -*- coding:utf-8 -*-
''''''

'''

Queue（线程安全队列类），有3种队列：

    1、FIFO（first in first out）先入先出队列 Queue
    2、LIFO（last in first out）后入先出队列 LifoQueue
    3、优先级队列（队列中可以设置优先级） PriorityQueue
    
    

常用的方法：

    Queue.qsize() 返回队列的大小
    Queue.empty() 如果队列为空，返回True,反之False
    Queue.full() 如果队列满了，返回True,反之False
    Queue.get([block[, timeout]]) 获取队列，timeout等待时间
    Queue.get_nowait() 相当Queue.get(False)
    非阻塞 Queue.put(item) 写入队列，timeout等待时间
    Queue.put_nowait(item) 相当Queue.put(item, False)
    


备注：

    当一个队列为空的时候如果再用get取则会堵塞，所以取队列的时候一般是用到

    get_nowait()方法，这种方法在向一个空队列取值的时候会抛一个Empty异常

    所以更常用的方法是先判断一个队列是否为空，如果不为空则取值
    

'''


from Queue import Queue
import threading,sys

queue = Queue()

def test():
    while True:
        global queue
        value = queue.get()
        if value % 100 == 0:
            print('%s ended - queue.get() = %d' % (threading.currentThread().name, value))
            break
        print('%s - queue.get() = %d' % (threading.currentThread().name, value))

for i in range(1,401):
    queue.put(i)

for i in range(4):
    t = threading.Thread(target=test)
    t.start()

