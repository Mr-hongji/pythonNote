# -*- coding:utf-8 -*-
''''''
'''
    
    类属性
        
        * 可以被继承
        
        * 调用方式：类名.属性
        
        * 只能由类进行修改或删除

'''

class A():
    name = 'A'

    def __init__(self):
        self.color = '白色'


a1 = A()
print('a1.name = %s' % a1.name)
print('A.name = %s' % A.name)

'''
    
    结果：
    
        a1.name = A
        A.name = A
        
    代码解析：
    
        类属性由类调用如：类名.属性， 所以 A.name = A 好理解，但是，在 a1 对象中没有属性name，
        为什么输出结果也是 A ？

'''

a1.name = 'B'
print('a1.name = %s' % a1.name) # a1.name = B
print('A.name = %s' % A.name) # A.name = A

A.name = 'C'
print('a1.name = %s' % a1.name) # a1.name = B
print('A.name = %s' % A.name)  # A.name = C