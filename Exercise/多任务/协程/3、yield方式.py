# -*- coding:utf-8 -*-
''''''

'''

yild:
    
    是使用的构造器方式来实现协程
    
'''

def A():
    print('A.....')
    yield
    print('A,,,,,')

def B():
    print('B.....')
    a.next()
    print('B,,,,,,')



a = A()
B()


'''

预想结果应该是这样：

    A.....
    B.....
    A,,,,,
    B,,,,,,


输出结果：

    B.....
    A.....
    B,,,,,,
    
    

不理解

'''