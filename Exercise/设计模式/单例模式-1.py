# -*- coding:utf-8 -*-
''''''


'''

    在Python中没有真正的单例

'''

class User():
    __instance = None

    def __init__(self,name):
        self.name = name
        pass

    @classmethod
    def getInstance(cls,name):
        if not cls.__instance:
           cls. __instance = User(name)
        return cls.__instance


u1 = User.getInstance('u1')
u2 = User.getInstance('u2')

# 同样可以直接通过new User对象进行创建对象
# 所以说Python中没有真正的单例模式
u3 = User('u3')

print('u1 = %s, u1.name = %s\nu2 = %s, u2.name = %s\n'
      'u3 = %s, u3.name = %s' % (u1, u1.name, u2, u2.name, u3,u3.name))


'''
    
    执行结果：
        
        u1 = <__main__.User instance at 0x024565F8>, u1.name = u1
        u2 = <__main__.User instance at 0x024565F8>, u2.name = u1
        u3 = <__main__.User instance at 0x024566E8>, u3.name = u3

    u1 和 u2 的内存地址是一致的
    
    u3 和 u1、u2 内存地址不一样，它们不是同一对象
    
'''