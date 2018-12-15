# -*- coding:utf-8 -*-

''''''

'''

multiprocessing:

    * 跨平台版本的多进程模块
    
    * 该模块提供了一个Process类来代表一个进程对象
    
'''

'''

Process:

    *   Process(target=run_proc, args=('test',), name = '', kwargs = {}, group)
    
            -   target线程的执行函数
    
            -   args执行函数的参数
            
            -   kwargs字典参数
            
            -   name当前进程实例的名称，如果不传默认是：Process-1,Process-2...
            
            -   group大多数情况用不到
        
    *   start():启动线程
    
    *   join():可以等待子进程结束后再继续往下执行，通常用于进程间同步
    
    *   join([timeout])
    
            - timeout：超时时间（秒），父进程等待子进程多少秒，
            如果到了这个时间，子进程没结束，父进程开始继续向下执行
    
    *   is_alive():判断进程实例是否还在执行(活着)
    
    *   run():如果在对象调用start()方法时，没有给定target参数，就将执行对象中的run()方法
    
    *   terminate():终止进程，父进程调用子进程

    * daemon = True | False ：设置进程为守护进程

'''

from multiprocessing import Process #注意： 是Process 不是process， P是大写
import os

def run_proc(name):
    print('Run Child process %s(%s)...' % (name, os.getpid()))

if __name__ == '__main__':
    print('Parent process %s..' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start...')
    p.start()
    p.join()
    print('Child process end...')


'''

运行结果：

    Parent process 9864..
    Child process will start...
    Run Child process test(10128)...
    Child process end...

'''

import time

def run_Child_Prcesss(name,num,**kwargs):
    print('子进程: name = %s, num = %s' % (name,num))
    for (k,v) in kwargs.items():
        print('子进程：(%s,%s)' % (k,v))
        time.sleep(2)

if __name__ == '__main__':
    pp = Process(name = 'Process-cp',target=run_Child_Prcesss,
                 args=('childProcess','10',),kwargs = {'A':1,'B':2})
    pp.start()
    pp.join(1) # 设置超时时间 子进程中设置里2秒等待，此处设置1秒
    pp.terminate() # 强制停止子进程
    print('子进程 name = %s' % pp.name)


'''

    执行结果：
    
        子进程: name = childProcess, num = 10
        子进程：(A,1)
        子进程 name = Process-cp

'''


if __name__ == '__main__':

    print('不指定 target 参数, 调用 strat()方法时，会默认执行Process的run方法...')
    pp = Process(name = 'Process-cp',
                 args=('childProcess','10',),kwargs = {'A':1,'B':2})
    pp.start()
    pp.join()
    print('子进程 name = %s' % pp.name)