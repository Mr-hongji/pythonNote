# -*- coding:utf-8 -*-
''''''


'''

    在多线程环境下，每个线程都有自己的数据。
    
    一个线程使用自己的局部变量比使用全局变量好，因为局部变量只有线程自己能看见，
不会影响其他线程，而全局变量的修改必须加锁。

    但是局部变量在函数调用的时候，传递起来很麻烦，如下代码：
    
'''

# 局部变量函数间传递方式

class Student():
    def __init__(self,name):
        self.name = name

def do_subtask_1(std):
    print('do_subtask_1')

def do_subtask_2(std):
    print('do_subtask_2')

def process_student(name):
    std = Student(name) # std是局部变量，但是每个函数都要用它，因此必须传进去
    do_task_1(std)
    do_task_2(std)

def do_task_1(std):
    do_subtask_1(std)
    do_subtask_2(std)

def do_task_2(std):
    do_subtask_2(std)
    do_subtask_2(std)



'''

        实际生产环境中，我们可能会调用很多函数，每个函数都需要很多局部变量，
    这时候用传递参数的方法会很不友好。

        为了解决这个问题，一个直观的的方法就是建立一个全局字典，
    保存进程 ID 到该进程局部变量的映射关系，运行中的线程可以根据自己的 ID 
    来获取本身拥有的数据。这样，就可以避免在函数调用中传递参数，如下示例：
     
     
     
        *   本身是一个全局变量，但是每个线程却可以利用它来保存属于自己的私有数据，
        这些私有数据对其他线程也是不可见的。

'''
import threading

global_dict = {}

def std_thread(name):
    std = Student(name)
    # 把std放到全局变量global_dict中：
    global_dict[threading.current_thread()] = std
    do_task_1()
    do_task_2()

def do_task_1():
    # 不传入std，而是根据当前线程查找：
    std = global_dict[threading.current_thread()]
    print(threading.current_thread(), std.name)

def do_task_2():
    # 任何函数都可以查找出当前线程的std变量：
    std = global_dict[threading.current_thread()]


'''

    保存一个全局字典，然后将线程标识符作为key，相应线程的局部数据作为 value，
这种做法并不完美。首先，每个函数在需要线程局部数据时，都需要先取得自己的线程ID，
略显繁琐。
    
    更糟糕的是，这里并没有真正做到线程之间数据的隔离，因为每个线程都可以读取到
全局的字典，每个线程都可以对字典内容进行更改。

'''


'''

    ThreadLocal 变量:

        为了更好解决这个问题，python 线程库实现了 ThreadLocal 变量(很多语言
    都有类似的实现，比如Java)。ThreadLocal 真正做到了线程之间的数据隔离，
    并且使用时不需要手动获取自己的线程 ID，如下示例：
    
'''


# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

'''

执行结果：
    
    Hello, Alice (in Thread-A)
    Hello, Bob (in Thread-B)

'''


'''

代码解析：

    threading.local() ： 创建全局的 ThreadLocal 对象
    
    local_school.student = name：
    
        * 存储一个变量到当前线程，如果在另外一个线程里面对 local_school.student
    进行赋值，那么会在另外一个线程单独创建内存空间来存储，也就是说在不同线程里面赋值，
    不会覆盖之前的值，因为每个线程里面都有一个单独的空间来保存这个数据，
    而且这个数据是隔离的，其它线程无法访问
    
    
        你可以把 local_school 看成全局变量，但每个属性如 local_school.student 
    都是线程的局部变量，可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal
    内部会处理。
    
    
        ThreadLocal 最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，
    用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访
    问这些资源
    
'''