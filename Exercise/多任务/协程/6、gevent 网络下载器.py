# -*- coding:utf-8 -*-

''''''

'''

gevent 库中有 一个 Monkey模块：

'''

import gevent,urllib

from gevent import monkey

# 有 IO 操作时需要这句话
#
monkey.patch_all()

def download(urlStr):
    print(urlStr)
    res = urllib.urlopen(urlStr)
    contentMsg = res.read()
    print('from %s read %d byte data' %(urlStr, len(contentMsg)))




g2 = gevent.spawn(download,'https://blog.csdn.net/shihongji/article/details/80974922')
g3 = gevent.spawn(download, 'https://cuiqingcai.com/category/technique/python')
g1 = gevent.spawn(download, 'http://www.baidu.com')


# gevent 提供了joinall 函数，以方便一次join多个
# 也可以一个一个的join

# g2 = gevent.spawn(download,'https://blog.csdn.net/shihongji/article/details/80974922')
# g3 = gevent.spawn(download, 'https://cuiqingcai.com/category/technique/python')
# g1 = gevent.spawn(download, 'http://www.baidu.com')

# g1.join()
# g2.join()
# g3.join()


gevent.joinall([

    gevent.spawn(download,'https://blog.csdn.net/shihongji/article/details/80974922'),
    gevent.spawn(download, 'https://cuiqingcai.com/category/technique/python'),
    gevent.spawn(download, 'http://www.baidu.com')

])



'''

执行结果：

https://blog.csdn.net/shihongji/article/details/80974922
https://cuiqingcai.com/category/technique/python
http://www.baidu.com

from https://cuiqingcai.com/category/technique/python read 56303 byte data
from http://www.baidu.com read 117123 byte data
from https://blog.csdn.net/shihongji/article/details/80974922 read 205292 byte data


'''