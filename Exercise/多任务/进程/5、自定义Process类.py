# -*- coding:utf-8 -*-
''''''

from multiprocessing import Process

import os,time

class CustomProcess(Process):
    def __init__(self):
        super(CustomProcess, self).__init__()


    # 重写 run 方法
    def run(self):
        time.sleep(3)
        print('子进程...')
        print('子进程id = %d， 父进程id =' % (os.getpid()))



if __name__ == '__main__':

    p = CustomProcess()
    p.start()
    p.join()
    print('子进程结束...')
    print('父进程id = %s' % os.getpid())

