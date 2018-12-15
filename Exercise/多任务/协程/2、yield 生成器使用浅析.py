# -*- coding:utf-8 -*-
''''''



'''

可能听说过，带有 yield 的函数在 Python 中被称之为 generator（生成器），何谓 generator ？

生成器的用处主要可以迭代

当一个函数中含有yield时,它不再是一个普通的函数,而是一个生成器.当该函数被调用时不会自动执行

先抛开 generator，以一个常见的编程题目来展示 yield 的概念。

'''

'''

如何生成斐波那契數列

    斐波那契（Fibonacci）數列是一个非常简单的递归数列，除第一个和第二个数外，
任意一个数都可由前两个数相加得到。用计算机程序输出斐波那契數列的前 N 个数是一个非常简单的问题，
许多初学者都可以轻易写出如下函数：


清单 1. 简单输出斐波那契數列前 N 个数

'''

def fab(max):
   n, a, b = 0, 0, 1
   while n < max:
       print b
       a, b = b, a + b
       n = n + 1


fab(5)

'''

执行 fab(5)，我们可以得到如下输出：
  
    1 
    1 
    2 
    3 
    5

    结果没有问题，但有经验的开发者会指出，直接在 fab 函数中用 print 打印数字会导致该函数可复用性较差，
因为 fab 函数返回 None，其他函数无法获得该函数生成的数列。

要提高 fab 函数的可复用性，最好不要直接打印出数列，而是返回一个 List。以下是 fab 函数改写后的第二个版本：

清单 2. 输出斐波那契數列前 N 个数第二版

'''
       

def fab(max):
   n, a, b = 0, 0, 1
   L = []
   while n < max:
       L.append(b)
       a, b = b, a + b
       n = n + 1
   return L


for n in fab(5):
    print n


'''

执行 for n in fab(5) 输出：

    1 
    1 
    2 
    3 
    5
    
        改写后的 fab 函数通过返回 List 能满足复用性的要求，但是更有经验的开发者会指出，
    该函数在运行中占用的内存会随着参数 max 的增大而增大，如果要控制内存占用，最好不要用 List
    来保存中间结果，而是通过 iterable 对象来迭代。例如，在 Python2.x 中，代码：

清单 3. 通过 iterable 对象来迭代

'''

for i in range(1000): pass

'''

会导致生成一个 1000 个元素的 List，而代码：

'''

for i in xrange(1000): pass

'''

则不会生成一个 1000 个元素的 List，而是在每次迭代中返回下一个数值，内存空间占用很小。
因为 xrange 不返回 List，而是返回一个 iterable 对象。

'''


def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # print b
        a, b = b, a + b
        n = n + 1

for n in fab(5):
    print n


'''

        yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，
    Python 解释器会将其视为一个generator，调用 fab(5) 不会执行 fab 函数，而是返回一个 iterable 对象！
    在 for 循环执行时，每次循环都会执行 fab 函数内部的代码，执行到 yield b 时，fab 函数就返回一个迭代值，
    下次迭代时，代码从 yield b 的下一条语句继续执行，而函数的本地变量看起来和上次中断执行前是完全一样的，于是函数继续执行，
    直到再次遇到 yield。

        也可以手动调用 fab(5) 的 next() 方法（因为 fab(5) 是一个 generator 对象，
    该对象具有 next() 方法），这样我们就可以更清楚地看到 fab 的执行流程：

清单 6. 执行流程
    
'''

f = fab(5)

f.next() # 输出  1

f.next() # 输出 1

f.next() # 输出 2

f.next() # 输出 3

f.next() # 输出 5

f.next() # 输出 Traceback (most recent call last): File "<stdin>", line 1, in <module> StopIteration

'''

        当函数执行结束时，generator 自动抛出 StopIteration 异常，表示迭代完成。
        在 for 循环里，无需处理 StopIteration 异常，循环会正常结束。
    
    我们可以得出以下结论：
    
        yield就是 return 返回一个值，并且记住这个返回的位置，下次迭代就从这个位置后(下一行)开始。
    
        一个带有 yield 的函数就是一个 generator，它和普通函数不同，生成一个 generator 看起来像函数调用，
    但不会执行任何函数代码，直到对其调用 next()（在 for 循环中会自动调用 next()）才开始执行。
    虽然执行流程仍按函数的流程执行，但每执行到一个 yield 语句就会中断，并返回一个迭代值，下次执行时从 yield 
    的下一个语句继续执行。看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，
    每次中断都会通过 yield 返回当前的迭代值。
    
        yield 的好处是显而易见的，把一个函数改写为一个 generator 就获得了迭代能力，
    比起用类的实例保存状态来计算下一个 next() 的值，不仅代码简洁，而且执行流程异常清晰。
    
    如何判断一个函数是否是一个特殊的 generator 函数？可以利用 isgeneratorfunction 判断：
    
清单 7. 使用 isgeneratorfunction 判断

'''


from inspect import isgeneratorfunction

isgeneratorfunction(fab) # 输出 True

'''

    要注意区分 fab 和 fab(5)，fab 是一个 generator function，而 fab(5) 是调用 fab 返回的一个 generator，
好比类的定义和类的实例的区别：

清单 8. 类的定义和类的实例

'''


import types
isinstance(fab, types.GeneratorType) # 输出 False

isinstance(fab(5), types.GeneratorType) # 输出 True


'''

fab 是无法迭代的，而 fab(5) 是可迭代的：

'''


from collections import Iterable

isinstance(fab, Iterable) # 输出 False

isinstance(fab(5), Iterable) # 输出 True


'''

每次调用 fab 函数都会生成一个新的 generator 实例，各实例互不影响：

'''

f1 = fab(3)
f2 = fab(5)

print 'f1:', f1.next() # 输出 f1: 1

print 'f2:', f2.next() # 输出 f2: 1

print 'f1:', f1.next() # 输出 f1: 1

print 'f2:', f2.next() # 输出 f2: 1

print 'f1:', f1.next() # 输出 f1: 2

print 'f2:', f2.next() # 输出 f2: 2

print 'f2:', f2.next() # 输出 f2: 3

print 'f2:', f2.next() # 输出 f2: 5



'''
return 的作用:

        在一个 generator function 中，如果没有 return，则默认执行至函数完毕，如果在执行过程中 return，
    则直接抛出 StopIteration 终止迭代。

另一个例子:

        另一个 yield 的例子来源于文件读取。如果直接对文件对象调用 read() 方法，会导致不可预测的内存占用。
    好的方法是利用固定长度的缓冲区来不断读取文件内容。通过 yield，我们不再需要编写读文件的迭代类，
    就可以轻松实现文件读取：

清单 9. 另一个 yield 的例子

'''


def read_file(fpath):
   BLOCK_SIZE = 1024
   with open(fpath, 'rb') as f:
       while True:
           block = f.read(BLOCK_SIZE)
           if block:
               yield block
           else:
               return


'''

    如一个函数中出现多个yield则next()会停止在下一个yield前:

'''

def fun2():
    print 'first'
    yield 5
    print 'second'
    yield 23
    print 'end...'

g1 = fun2()
g1.next()   # 第一次运行,暂停在yield 5
# 输出 first
# 输出 5

g1.next()  # 第二次运行,暂停在yield 23
# 输出 second
# 输出 23

g1.next() # 第三次运行,由于之后没有yield,再次next()就会抛出错误
# 输出 end...
# 输出 Traceback (most recent call last): File "<stdin>", line 1, in <module> StopIteration


'''

    next() 和  send(None)

        send(msg)与next()的区别在于send可以传递参数给yield表达式，这时传递的参数会作为yield表达式的值，
    而yield的参数是返回给调用者的值。——换句话说，就是send可以强行修改上一个yield表达式值。
    比如函数中有一个yield赋值，a = yield 5，第一次迭代到这里会返回5，a还没有赋值。第二次迭代时，使用.send(10)，
    那么，就是强行修改yield 5表达式的值为10，本来是5的，那么a=10
    
        send(msg)与next()都有返回值，它们的返回值是当前迭代遇到yield时，yield后面表达式的值，
    其实就是当前迭代中yield后面的参数。



'''


def fun():
    print 'start...'
    m = yield 5
    print m
    print 'middle...'
    d = yield 12
    print d
    print 'end...'

m = fun() # 创建一个对象

m.next() # 会使函数执行到下一个yield前
# 输出 start...
# 输出 5

m.send('message') # 利用send()传递值
# 输出 message   # send()传递进来的
# 输出 middle...
# 输出 12

m.next()
# 输出 None  # 可见next()返回值为空
# 输出 end...
# 输出 Traceback (most recent call last): File "<stdin>", line 1, in <module> StopIteration





'''

以上仅仅简单介绍了 yield 的基本概念和用法，yield 在 Python 3 中还有更强大的用法

'''