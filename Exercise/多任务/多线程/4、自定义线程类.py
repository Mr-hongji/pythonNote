# -*- coding:utf-8 -*-
''''''
'''

    自定义进程类，只需要继承 threading.Thread ,然后重写 run 方法

'''

import threading,time

class CustormThread1(threading.Thread):

    def __init__(self,name):
        super(CustormThread1, self).__init__()
        # self.setName(name)
        self.name = name

    def run(self):
        for i in range(3):
            # 在自定义线程类中 获取当前线程的名称可以使用：
            # threading.currentThread().name
            # 或
            # self.name
            print('thread name = %s, i = %d' % (threading.currentThread().name, i))
            time.sleep(1)



if __name__ == '__main__':
    print('mainThread Running...')
    t1 = CustormThread1('childThread')
    t1.start()
    t1.join()
    print('childThread run ended...')


