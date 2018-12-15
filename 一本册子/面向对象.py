'''

    通过dir()方法可以查看一个类/变量的所有属性

'''

s = 'I\'m Shihongji' #s被赋值后就是一个字符串类型的对象

print dir(s)

l = s.split() #split是字符串的方法，这个方法返回一个list类型的对象, l是一个list类型的对象

print dir(l)


'''

    语法格式：

        class className:

        * 类方法的第一个参数必须是self
        * 调用类方法的时候，只需要 对象.方法名()
        * 不需要额外提供self这个参数值

'''


class MyClass:
    name = '侍洪洪'
    
    def sayHi(self):
        print 'hello ' + self.name  #注意这个地方 是 self.name 不能直接写name (直接写name是访问的全局变量)


mc = MyClass()

print mc.name

mc.name = '洪洪'

mc.sayHi()
