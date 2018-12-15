# -*- coding: cp936 -*-
'''

    打开远程文件


        * 使用的是urllib中的urlopen函数

        * urlopen返回的对象同样支持close、read、readline和readlines方法

        * 访问本地文件的格式 'file:d://PythonWorkSpace/guestNumberGame.txt'

'''

from urllib import *

f = urlopen('http://www.baidu.com')
print f.read()
f.close()


f = urlopen('file:d://PythonWorkSpace/guestNumberGame.txt')
print f.read()
f.close()
