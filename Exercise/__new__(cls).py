# -*- coding:utf-8 -*-
''''''

'''

    __new__(cls)方法:
        
        * 参数是 cls (类)，不是 self
        * 必须要有返回值

'''

class User(object): # 正规写法： 类没有继承时就用object代替
    def __init__(self):
        print('对象初始化')

    # 重写 new() 方法
    def __new__(cls):
        print('开始创建对象')
        return object.__new__(cls) # 使用object父类，创建对象


u = User()

print u

'''

    执行结果：
        
        开始创建对象
        对象初始化
        <__main__.User object at 0x02409D30>
        
    如果__new__()方法中没有返回值，将不会执行__init__()方法

'''
