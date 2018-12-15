# -*- coding:utf-8 -*-
''''''

'''

    使用 __new__(cls) 方法实现单例

'''

class User(object): # 养成习惯：没有继承的类就用object代替

    __instance = None

    def __init__(self,name):
        self.name = name

    def __new__(cls, name):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance


u1 = User('name1') # 1
u2 = User('name2') # 2


print('u1 = %s, u1.name = %s\nu2 = %s, u2.name = %s '
      '' % (u1,u1.name,u2,u2.name))


'''

    执行结果：
    
        u1 = <__main__.User object at 0x023D9D30>, u1.name = name2
        u2 = <__main__.User object at 0x023D9D30>, u2.name = name2 

    这一次 u1 和 u2 的 name 仍然相同，但是，只是 name 的值 都变成了 name2

    代码解析：
    
        User('name1')时，调用__new__()创建对象并返回后，执行__init__()方法，
        这时 __instance 对象的 name 被赋值为: name1
        
        执行 User('name1')时，同样调用了__new__()方法，虽然 这时候 __instance 对象不为空，
        但是还是会返回，并且执行 __init__()方法，这时 __instance 对象的 name 属性
        就被重新赋值为 ： name2
        
        所以，最后是 u1 和 u2 的 name 值都是： name2

'''