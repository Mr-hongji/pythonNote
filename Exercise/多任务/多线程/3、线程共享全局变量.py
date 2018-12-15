# -*- coding:utf-8 -*-
''''''

'''

例1：线程使用全局变量

'''

import threading

g_num = 10

def work1():
    for i in range(3):
        global  g_num
        g_num += 1
        print('work1 g_num = %d' % g_num)

def work2():
    print('work2 g_num = %d' % g_num)


print('mainWork1 g_num = %d' % g_num)

w1 = threading.Thread(target=work1)
w1.start()
w1.join()

w2 = threading.Thread(target=work2)
w2.start()
w2.join()


'''

    执行结果：
    
        mainWork1 g_num = 10
        work1 g_num = 11
        work1 g_num = 12
        work1 g_num = 13
        work2 g_num = 13
        
    work1 和 work2 可以同时访问 g_num

'''


'''

例2：用传参的方式使用全局变量


'''

print('')


g_num = 10

def work3(num):
    for i in range(3):
        num += 1
        print('work3 num = %d, g_num = %d' % (num, g_num))


def work4(num):
    print('work4 num = %d, g_num = %d' % (num, g_num))


print('mainWork2 g_num = %d' % g_num)

w3 = threading.Thread(target=work3,args=(g_num,))
w3.start()
w3.join()

w4 = threading.Thread(target=work4,args=(g_num,))
w4.start()
w4.join()

print('mainWork2 chidWork ended, g_num = %d' % g_num)


'''

执行结果：

    mainWork2 g_num = 10
    work3 num = 11, g_num = 10
    work3 num = 12, g_num = 10
    work3 num = 13, g_num = 10
    work4 num = 10, g_num = 10
    mainWork2 chidWork ended, g_num = 10
    

代码解析：

    num 的值只在 work3 中改变了值， 全局变量 g_num 的值没有发生改变，
    因为在把 g_num 变量以参数的方式传入 work3 中时， 在 work3 中使用的 num 实际被转换成了
    work3 中的 局部变量，所以改变 num 的值时，不会影响全局变量的值
    
'''



'''

例3：把全局变量 g_num 改成列表，然后以传参的方式使用

'''

print('')

g_num = [1,2,3]

def work5(num1):
    num = num1
    for i in range(3):
        num.append(4)
        print('work3 num = %s, g_num = %s' % (str(num), str(g_num)))


def work6(num):
    print('work4 num = %s, g_num = %s' % (str(num), str(g_num)))


print('mainWork3 g_num = %s' % str(g_num))

w5 = threading.Thread(target=work5,args=(g_num,))
w5.start()
w5.join()

w6 = threading.Thread(target=work6,args=(g_num,))
w6.start()
w6.join()

print('mainWork2 chidWork ended, g_num = %s' % str(g_num))

'''

运行结果：

    mainWork3 g_num = [1, 2, 3]
    work3 num = [1, 2, 3, 4], g_num = [1, 2, 3, 4]
    work3 num = [1, 2, 3, 4, 4], g_num = [1, 2, 3, 4, 4]
    work3 num = [1, 2, 3, 4, 4, 4], g_num = [1, 2, 3, 4, 4, 4]
    work4 num = [1, 2, 3, 4, 4, 4], g_num = [1, 2, 3, 4, 4, 4]
    mainWork2 chidWork ended, g_num = [1, 2, 3, 4, 4, 4]
    

代码解析：

    全局变量 g_num 最后的值也被改变了，因为 g_num 是一个可变对象，可变变量作为参数传值时，
    
    传的实质是该变量的内存引用

'''


'''

可变对象和不可变对象参考 ： 可变对象和不可变对象.py

'''