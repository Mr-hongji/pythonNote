# -*- coding:utf-8 -*-
''''''
'''

    greenlet 方式
    
    使用greenlet需要注意一下三点：

        第一：greenlet创生之后，一定要结束，不能switch出去就不回来了，否则容易造成内存泄露。

        第二：python中每个线程都有自己的main greenlet及其对应的sub-greenlet ，
        不能线程之间的greenlet是不能相互切换的。

        第三：不能存在循环引用
    
    详细看： http://python.jobbole.com/87182/
             http://python.jobbole.com/88125/

'''


'''

greenlet这个module里面的属性:



['GREENLET_USE_GC', 'GREENLET_USE_TRACING', 'GreenletExit', '_C_API', '__doc__', '__file__', 
'__name__', '__package__', '__version__', 'error', 'getcurrent', 'gettrace', 'greenlet', 'settrace']


其中，比较重要的是getcurrent()， 类greenlet、异常类GreenletExit。

getcurrent()返回当前的greenlet实例；

GreenletExit：是一个特殊的异常，当触发了这个异常的时候，即使不处理，
            也不会抛到其parent（后面会提到协程中对返回值或者异常的处理）

'''
import greenlet

print dir(greenlet)



'''

greenlet.greenlet这个类:

['GreenletExit', '__class__', '__delattr__', '__dict__', '__doc__', '__format__',
 '__getattribute__', '__getstate__', '__hash__', '__init__', '__new__', '__nonzero__',
  '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 　　'__sizeof__', '__str__',
   '__subclasshook__', '_stack_saved', 'dead', 'error', 'getcurrent',
 'gettrace', 'gr_frame', 'parent', 'run', 'settrace','switch', 'throw']
 
 
 
比较重要的几个属性：

run：当greenlet启动的时候会调用到这个callable，如果我们需要继承greenlet.greenlet时，需要重写该方法

switch：前面已经介绍过了，在greenlet之间切换

parent：可读写属性，后面介绍

dead：如果greenlet执行结束，那么该属性为true

throw：切换到指定greenlet后立即跑出异常

'''

print dir(greenlet.greenlet)




from greenlet import greenlet




def A():

    while True:
        a = 1
        print('a,,,,,,, a = ' + str(a))

        fb.switch() # 切换到 fb 中执行

        a += 1
        print('A........ a = ' + str(a))

        fb.switch()

        break

def B():

    while True:
        b = 1
        print('B,,,,,,, b = ' + str(b))

        fa.switch() # 切换到 fa 中执行

        b += 1
        print('B........ b = ' + str(b))

        break



fa = greenlet(A)

fb = greenlet(B)

# 切换到 fa 执行
fa.switch()