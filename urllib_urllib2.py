# -*- coding: cp936 -*-
'''

    ��Զ���ļ�


        * ʹ�õ���urllib�е�urlopen����

        * urlopen���صĶ���ͬ��֧��close��read��readline��readlines����

        * ���ʱ����ļ��ĸ�ʽ 'file:d://PythonWorkSpace/guestNumberGame.txt'

'''

from urllib import *

f = urlopen('http://www.baidu.com')
print f.read()
f.close()


f = urlopen('file:d://PythonWorkSpace/guestNumberGame.txt')
print f.read()
f.close()
