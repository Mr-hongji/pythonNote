
'''

    __del__():
    

    调用场景：

        1、当删除对象时，Python解析器会默认调用__del__()方法

        2、销毁（释放）内存中的对象时回调__del__()方法

'''

class User():
    def __init__(self):
        print('User 初始化成功---')

    def __del__(self):
        print('User 对象被回收---')


# 创建一个user对象
u = User()

# 删除该User对象
del u

print('del u -------------')


'''

    执行结果：

        User 初始化成功---
        User 对象被回收---
        del u -------------


    代码解析：

        __del__() 方法在 print('del U -------------') 之前执行

        u = User() 在内存中创建了一个 User 对象，并且让变量 u 引用该内存的 User 对象

        del u 删除变量 u , 此时内存中的 User 对象没有任何变量，对其引用，Python解析器就会

        回调 __del__()方法，回收内存

'''

print('')


u1 = User()

u2 = u1

del u1

print('del u1 -------')

del u2

print('del u2 -------')


'''

    执行结果：

        User 初始化成功---
        del u1 -------
        User 对象被回收---
        del u2 -------


    代码解析：

        u1 = User() 创建一块存放 User 对象的内存，并且，变量 u1 指向该内存

        u2 = u1 此处又新建变量 u2, 并且 u2 引用了 u1 的内存地址，此时，u1 和 u2 同时，

        引用同一个内存地址

        del u1 删除 u1 时，删除该变量对的引用，此时，由于内存中的 User 对象还在被 u2 引用，

        所以不会回收该内存（不会回调__del__()方法）

        del u2 删除 u2 后，内存中的 User 已经没有引用的变量，此时解释器才会对内存进行回收，回调
        __del__()方法
 
'''

print('')


u3 = User()

print('u3 ------------')


'''

    pycharm中执行结果：

        User 初始化成功---
        u3 ------------
        User 对象被回收---
        
        
    Python自带的IDLE中执行结果：
    
         User 初始化成功---
         u3 ------------
         
        
    代码解析：
    
        程序执行结束，所以内存被回收
        
        使用 Python 自带的编译器运行时，如果 '__del__().py' 没有关闭，则 u3 所引用的内存就不会被销毁，所以在
        Python自带的IDLE中执行结果中不会打印  ‘User 对象被回收---’
    
'''


