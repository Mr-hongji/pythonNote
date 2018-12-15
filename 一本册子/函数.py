'''
    函数的定义

    关键词 def (define缩写)
'''

def hello():
    print 'Hello Shihongji'


hello()
hello()




'''
    函数参数方式一
        * def hello(参数1,参数2,参数3....)
'''

def sayHello(name):
    print 'Hello ' + str(name)

sayHello('Shihongji')
sayHello(123)




'''
    函数参数二（设置默认参数）
    
        * def hello(name='123')
        * 当函数有多个参数时，如果你想给部分参数提供默认参数，那么这些参数必须在参数的末尾。
        * def func(a, b=5)  可以
        * def func(a=5, b)  不可以
'''

def sayHello1(name = 'World'):
    print 'Hello ' + str(name)


sayHello1()
sayHello1("Shihongji")


'''
    猜数字游戏
'''

print '\n----猜数字游戏----\n'

from random import randint

def isEqual(num1, num2):
    if num1 < num2:
        print 'too small'
        return False
    if num1 > num2:
        print 'too big'
        return False
    if num1 == num2:
        print 'guest right'
        return True

randomNum = randint(0,100)

print '\n随机生成的数字: ' + str(randomNum) + '\n'

isOk = False

while not isOk:
    answer = input()
    isOk = isEqual(answer, randomNum)





'''

    函数参数方式三（元组参数）

        * def func(*args)
        
'''

def calcSum(*args):
    
    sum = 0
    
    for i in args:
        sum += i
        print i
        
    print sum


calcSum(1,2,3,4,5,6,7,8,9)






'''

    函数参数方式四（字典参数）

        * func(**kargs)
        * 把参数以键值对字典的形式传入
        * 字典是无序的，所以输出的结果不是按照顺序输出的
'''


def printAll(**args):
    for key in args:
        print key,':',args[key]
        print


printAll(a=1,b=2,c=3,d=4)





'''

    函数参数（四种方式混合使用）

        * 形参顺序(必须遵守)：func（无默认值形参, 有默认值形参, 元组参数*args, 字典参数**args）
        * 可以省略某种类型的参数，但仍需保证此顺序规则。


   在函数被调用时，参数的传递过程为：
   
        * 按顺序把无指定参数的实参赋值给形参；
        * 把指定参数名称(arg=v)的实参赋值给对应的形参；
        * 将多余的无指定参数的实参打包成一个 tuple 传递给元组参数(*args)；
        * 将多余的指定参数名的实参打包成一个 dict 传递给字典参数(**kargs)。
'''


def func(x,y=5,*a,**b):
    print x,y,a,b


func(1) #结果：1 5 () {}

func(1,2) #结果：1 2 () {}

func(1,2,3) #结果：1 2 (3,) {}

func(1,2,3,4) #结果：1 2 (3, 4) {}

func(x=1) #结果：1 5 () {}

func(x=1,y=1) #结果：1 1 () {}

func(x=1,y=1,a=1) #结果：1 1 () {'a': 1}

func(x=1,y=1,a=1,b=1) #结果：1 1 () {'a': 1, 'b': 1}

func(1,y=1) #结果：1 1 () {}

func(1,2,3,4,a=1) #结果：1 2 (3, 4) {'a': 1}

func(1,2,3,4,k=1,t=2,o=3) #结果：1 2 (3, 4) {'k': 1, 't': 2, 'o': 3}








