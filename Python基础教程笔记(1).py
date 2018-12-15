#encoding=GBK
 #------------------------------------- 第一章 ------------------------------------#


print
print '第一章'

'''

    * 整数 / 整数, 计算结果的小数部分被截除，只保留整数部分（不会四舍五入） 如：  1 / 2

    * 实数在Python中成为浮点数（Float）
    * 参与除法的两个数中有一个数为浮点数，结果也为浮点数 如： 1.0 / 2, 1 / 2.0,  1.0 / 2.0

    * 通常情况下只需要普通算法，即 1 / 2 = 0.5 ,方法如下：
        * 在程序前加上 from __future__ import division (__future__ 前后是两个下划线)
        * 或直接在解析器中执行它

    * 幂运算 （2 ** 3） 
  
'''

print  1 / 2 #结果 0

print 1.0 / 2 #结果 0.5
print 1 / 2.0 #结果 0.5
print 1.0 / 2.0 #结果 0.5

print 2 ** 3 #结果 8



'''

    转换字符串的两种机制

        * str（）函数，把值转换为合理的字符串形式 ----- 常用此方式
        * repr（）函数，创建一个字符串

'''

temp = 10

print 'The temperature is: ' + str(temp)
print 'The temperature is: ' + repr(temp)



'''

    原始字符串输出 r
    
'''

print 'Hello\nWorld' # 结果会换行 因为\n是换行符
print 'Hello''World'
print 'Hello','World'
print 'Hello World'

print 'C:\nowhere' 

# 此时如果想完整打印路径需要使用 r 原始字符标识

print r'C:\nowhere'
print r'C:\nowhere\\'
print r'C:\nowhere' '\\'

print r'Let\'s go!' # 输出 Let\'s go!

#或

print 'C:\\nowhere' # 此方式不适合长字符串 如： C:\\nwhere\\bozz\\frozz  需要写很多反斜杠






 #------------------------------------- 第二章 ------------------------------------#

print
print '第二章'



'''
    列表步长

        * 步长可以是正数或负数，但不能是0
        * 步长是负数时，开始点索引必须大于结束点索引 numbers[8:3:-2] 8(开始索引) > 3（结束点索引）
        * 步长是负数时，则从序列尾部向左提取元素，直到第一个元素
        * 步长是正数时，则从序列的头部开始向右提取元素
'''

numbers = [1,2,3,4,5,6,7,8,9,10]

print numbers[:5:1] # [1,2,3,4,5] 步长设置为1 （默认就是1）

print numbers[:5:2] # [1,3,5]

print numbers[8:3:-2] # [9,7,5]




'''

    序列相加

        * 两种相同类型的序列才能进行连接操作

'''

print [1,2,3] + [4,5,6]



'''

    乘法

        这是一个很神奇的地方
'''

print 'Python' * 5 # 等同于 'Python' + 'Python' + 'Python' + 'Python' + 'Python'

print [10] * 5 # 利用了序列相加 等同于 [10] + [10] + [10] + [10] + [10] 




'''

    in 运算符

        * 检查一个值是否在序列中
        * 存在返回True  不存在返回False
    
'''

name = '侍洪洪'

print '洪' in name
print '洪吉' in name

names = ['侍洪洪', '侍不是傻', '侍洪吉']

print '侍洪洪' in names

print '洪吉' in names


database = [
    ['honghong', '123'],
    ['hongji', '1234'],
    ['shihongji', '000000']
]

name = raw_input('输入用户名:')
pin = raw_input('PIN码:')
if [name,pin] in database:
    print 'User Acc granted'


'''

    len() 返回列表长度
       
    min() 返回列表中最小元素
    
    max() 返回列表中最大元素

    max和min参数并不是一个序列，是以多个数字直接作为参数

    list() 把字符串强转成字符数组

'''
#l = [10,4,7,2,3,0]
l = ['shihongji', 'shihonghong', 'shixiaohong']
print len(l)
print min(l)
print max(l)

print min(1,5,2,1)
print max(1,5,2,3)

print list('shi') #输出['s','h','i'] 




'''

    切片赋值
    
'''

name = list('shihongji')

name[7:] = list('hong') # ['s', 'h', 'i', 'h', 'o', 'n', 'g', 'h', 'o', 'n', 'g']
print name

numbers = [1,2,4,5]
numbers[1:3] = [3]
print numbers

numbers = [3,1,4,5,8,10]
print numbers[:3:2] #输出[3,4]
numbers[:3:2] = [9] * 2 #实际就是把[3,4] 替换赋值 [9] * 2 步数是几就乘几
print numbers



'''

    extend() 在列表末尾一次性追加另一个序列中的多个值

    a.extend(b) extend函数修改了被扩展的列（例子中的a）

    a + b 会生成一个新的列表(例子中的c)
'''

a = [1,2,3]
b = [4,5,6]

a.extend(b) # 把b列表元素追加到a列表后

print a

a = [9,8,7]
b = [4,5,6]

c = a + b
print a
print b
print c


'''

    index(元素值) 返回元素在列表中的索引

    insert（要插入的索引位置, 元素值）向列表中插入元素

    pop() 移出列表元素（默认移出最后一个），并返回该元素的值
    pop(0) 移出列表第0个元素

    remove() 移出列表中的某个值

    reverse() 将列表中的数据反向存放 [1,2,3] reverse() 后 变成[3,2,1]

    list.sort() 和 sorted(list) 排序(默认升序排序)：

        * sort() 对原列表排序，会改变原列表
        * sorted() 排序后会生成新的列表，原列表不变
'''

l = [1,2,3,'shi', 'hong', 'ji']

index = l.index('shi')
print index # 3

l.insert(0, 'honghong')
print l # ['honghong', 1, 2, 3, 'shi', 'hong', 'ji']

l.pop()
print l # ['honghong', 1, 2, 3, 'shi', 'hong']

l.pop(0)
print l # [1, 2, 3, 'shi', 'hong']

l.remove('hong')
print l # [1, 2, 3, 'shi']

l.reverse()
print l # ['shi', 3, 2, 1]

l = [2,3,5,'shi', 'hong', 'ji']
l.sort()
print l # [2, 3, 5, 'hong', 'ji', 'shi']

l = [2,3,5,'shi', 'hong', 'ji']
ll = sorted(l)
print l # [2, 3, 5, 'shi', 'hong', 'ji']
print ll # [2, 3, 5, 'hong', 'ji', 'shi']



'''

    列表清空

        * l[:] = []
        * del l[:]
'''

l = ['1', '2', 3, 4]
print l
l[:] = []
print l

l = ['2', 's', 'f']
print l
del l[:]
print l

'''

    元组

        语法：
            1,2,3 或 （1,2,3）要用逗号分隔
                - 用逗号分割值，就是自动创建了元组

        * 和列表一样也是一种序列
        * 元组不能修改，没有像列表一样的方法

        元组元素访问同列表访问一致：

            yz = (1,2,3)
            yz[0]
            yu[:2]

'''

print 1,2,3 # 1,2,3

print (1,2,3) # (1,2,3)

print () # 空元组

print (42,) # (或 42,) 创建只有一个元素值的元组, 必须加逗号，即时只有一个值

print (40 + 2) * 3 # 126

print (40 + 2,) * 3 # (42,42,42) 是逗号改变了结果




'''

    tuple() 序列转元组，功能跟list()一样，都是类型强转

'''

print tuple([1,2,3])
print tuple('abc')







#------------------------------------- 第三章 ------------------------------------#





'''

    字符串格式化

        * %d、%s、%f

   
'''

format = 'doc.%s.%s.cn'
values = ['hongji', 'org']
print format % (values,values)


'''

 模板字符串

        * 是string模块提供的另外一种格式化值的方法

'''
from string import Template

s = Template('$x, shihongji $y!')
s = s.substitute(x = 'Hi', y = 'baobao')
print s # Hi, shihongji baobao!


# 替换单词的一部分
s = Template('I\'m shihong${x}')
s = s.substitute(x = 'ji')
print s # I'm shihongji


#使用字典变量替换
s = Template('$x is a $y')
d = {}
d['x'] = 'shihonghong'
d['y'] = 'liangmin'
s = s.substitute(d)
print s # shihonghong is a liangmin



#此处注意： %s是字符串格式化 1,1,2三个数均是int，程序在处理时会转成string
s = '%s plus %s equals %s' % (1,1,2) 
print s # 1 plus 1 equals 2



'''

    字段宽度和精度

        * 宽度是转换后的值所保留的最小字符个数
        * 精度是结果中应该报刘的小数位数（对字符串来说就是转换后的值所能包含的最大字符个数）
        * 这两个参数都是整数，用点号分隔
        * 如果只给出精度，就必须包含点号

    可以使用*作为字段宽度或者精度（或者两者都是用*），此时自断宽度或精度的数值会从元组参数中读取
        
'''

from math import pi

print '%10f' % pi # 10个字符宽度 输出：'    3.141593' 前面用空格补齐 
print '%10.2f' % pi # 10个字符宽度 精度是2 输出'       3.14' 前面用空格补齐
print '%.2f' % pi # 精度是2 输出： '3.14' 保留两位小数

# 对字符串来说就是转换后的值所能包含的最大字符个数
print '%.5s' % 'shihongji is a liangmin' # 输出 'shiho'


print '%.*s' % (5,'shihongji is a liangmin') # 从元组中取出精度是5 输出shiho

print '%010.2f' % pi #输出 0000003.14  字符宽度用0填充  010.2f(0:用0填充，10：字段宽，2:精度)

print '%-10.2f' % pi # 输出'3.14      '  -10.2f('-':靠左对齐)
print '%+10.2f' % pi # 输出'      +3.14'  +10.2f('+':靠右对齐)


'''

    字符串格式化练习

'''


width = 50 #list width

price_width = 10
item_width = width - price_width

head_format = '%-*s%*s'
format_data = '%-*s%*.2f'

print '=' * width

print head_format % (item_width, 'Item', price_width, 'Price')

print '-' * width

print format_data % (item_width, 'Apple', price_width, 1.586)
print format_data % (item_width, 'Pears', price_width, 1.92)
print format_data % (item_width, 'Cantaloupes', price_width, 2.2521)
print format_data % (item_width, 'Prunes', price_width, 1.98)


'''

使用中文时，格式会变乱  原因未知

print format_data % (item_width, '苹果', price_width, 1.58)
print format_data % (item_width, '梨', price_width, 1.92)
print format_data % (item_width, '苹果', price_width, 2.25)
print format_data % (item_width, '煎饼果子', price_width, 1.98)

'''


print '=' * width



'''

    字符串方法

        find(要查找的字符串，起始点，结束点) 查找字符串返回索引，找不到返回-1
        lower() 字符串转小写
        replace(被替换字符串，新字符串)
        strip() 清除字符串两端空格,也可以指定要去除的字符串
        split() 字符串分割
        join() 字符串拼接
'''

name = '$$$ Shihongji Is a Liangmin! $$$'
print name.find('$$$') # 0
print name.find('$$$',1) # 29  从索引1开始向后查找
print name.find('a',1,10) # -1 在索引1和10之间找不到a

name1 = name.lower() # 不会改变原name的值，会重新生成一个新的副本
print name1
print name

name1 = name.replace('Shihongji','Shihonghong')# 不会改变原name的值，会重新生成一个新的副本
print name1
print name

name = '   Shihongji Is a Liangmin!   '
print name
name1 = name.strip()# 不会改变原name的值，会重新生成一个新的副本
print name1

name = '*$$$ honghong Is a Liangmin! $$$*'
name1 = name.strip('*$') # 指定要去除的字符串 *$
print name1



#------------------------------------- 第四章 ------------------------------------#



'''

    创建字典

        * 直接使用{} 如： d = {}
        * 使用dict()函数
        
'''

#直接使用{}
d = {} #创建一个空字典
d = {'name':'shihonghong', 'age':30}
print d , d['age']

print 'name' in d # 检查字典中是否含有键为name的项

#使用dict()函数(通过关键字参数创建字典)
d = dict(name = 'shihongji', age = 30)
print d

##使用dict()函数(通过(键，值)这样的序列对创建字典
items = [('name','shibushisha'), ('age', 30)]
print items[0][0] # items[0]:输出元组('name','shibushisha') items[0][0] 输出:name
d = dict(items)
print d

'''

    使用字典格式化字符串

        %s%d % ('shihongji', 1) 这是前面用过的使用元组进行格式化字符串

'''

dic = {'name':'shihongji', 'age':30}
print '%(name)s\'s age is : %(age)d' % dic



'''

    字典方法 dic = {}

        * dic.clear() 清除内存中的字典数据,所有引用该内存字典的变量都会清空 返回None

        * dic.copy() (浅拷贝)  &  deepcopy(dict)(深拷贝)
            - 浅拷贝(copy)：拷贝父对象，不会拷贝对象的内部的子对象。
            - 深拷贝(deepcopy)：copy模块的deepcopy方法，完全拷贝了父对象及其子对象。
            - 详细解释参考：http://blog.csdn.net/u014647208/article/details/77683545

        * dic.fromkeys() 使用给定的键建立新的字典，每个键对应的值默认为None

        * dic.get(key) 访问字典项 同 dic[key]
            - 使用dic[key]访问字典中不存在的项时会出错
            - 使用dic.get(key)访问字典中不存在的项时，不会有异常，会返回None值

        * dic.items() 将所有的字典项以列表的形返回如：[(键，值),(键，值)...]

        * dic.iteritems() 作用与items()方法大致相同，但返回结果时迭代器不是列表，iteritems()效率更高

        * dic.keys() 将字典中的键以列表的形式返回如：[键，键，键...]

        * dic.iterkeys() 将字典中的键以迭代器的形式返回

        * dic.values() 以列表的形式返回字典中的值如：[值，值，值...]

        * dic.itervalues() 将字典中的值以迭代器的形式返回

        * dic.pop(键) 移除字典中的键值,返回被移除的元素的值
            - 列表中的l.pop(index)方法是通过索引移除列表中的元素
            - dic.pop(键)方法是通过键移除字典元素

        * dic.popitem() 类似于list.pop()移除最后一个元素
            - 由于字典的元素顺序不是固定的，所以'最后的元素'是不固定的
            - 如果要一个接一个的移除并处理元素可使用此方法

        * dic.setdefault(键，默认值)
            - 如果不设定默认值参数，同get()方法一样默认使用None
            - 类似于get()方法，能获得给定键相关联的值
            - 在字典中不包含给定键的情况下设定响应的键值
            - 当键不存在时，setdefault返回默认值并相应的更新字典
            - 如果键存在，则返回与其对应的值，不再改变字典键值

        * dic.update(新字典) 利用一个字典更新另一个字典
            - 提供的新字典中的项会被添加到旧字典中
            - 如果新字典中的项与旧字典中的项相同，则会进行覆盖
'''

# dic.clear()
d = {'name':'shihongji', 'sex':'男'}
print d
d.clear()
print d # 输出{}

# dic.copy()
x = {'name':'shihongji', 'age':30}
y = x.copy()
print  y #输出 {'name':'shihongji', 'age':30}

# deepcopy(dic)
from copy import deepcopy
a = {'name':'asd', 'age':20}
b = deepcopy(a)
print b #输出 {'name':'asd', 'age':20}

# dic.fromkeys()
a = {}
b = a.fromkeys(['name', 'sex'])
#或直接使用dict类调用fromkeys()方法
c = dict.fromkeys(['number', 'address'])
print a, b, c #输出 {} {'name': None, 'sex': None} {'number': None, 'address': None}
#如果键的默认值不想使用None，可以指定键的默认值
c = dict.fromkeys(['number', 'address'], 'defaultValue')
print c #输出 {'number': 'defaultValue', 'address': 'defaultValue'}

#dic.get(key)
a = {'phone':'111', 'address':'asd'}
print a['phone'], a.get('phone') #输出 111 111
print a.get('name') #输出 None
#get()方法可以自己定义默认值，替换None
print a.get("name", 'null') #输出 null
#print a['name'] #由于字典中没有name项所以，此行代码会报错

#dic.items()
a = {'name':'shihongji', 'age':30}
b = a.items()
print b #输出 [('age', 30), ('name', 'shihongji')]

#dic.iteritems()
b = a.iteritems()
print type(b), b #输出 <type 'dictionary-itemiterator'> <dictionary-itemiterator object at 0x02A9C240>
b = list(b) #Convert the iteratir to a list(迭代器转换成列表)
print b, list('asdf') #输出 [('age', 30), ('name', 'shihongji')] ['a', 's', 'd', 'f']

#dic.keys()
b = a.keys()
print b #输出 ['age', 'name']

#dic.iterkeys()
b = a.iterkeys()
b = list(b)#Convert the iteratir to a list(迭代器转换成列表)
print b #输出 ['age', 'name']

#dic.values()
b = a.values()
print b #[20, 'shihongji', 'boy']

#dic.itervalues()
b = a.itervalues()
b = list(b) #Convert the iteratir to a list(迭代器转换成列表)
print b #[30, 'shihongji']

#dic.pop()
c = a.pop('name')
print c, a #输出 shihongji {'age': 30}

#dic.popitem()
a = {'url':'www.baidu.com', 'spam':0, 'title':'baidu'}
print a.popitem() # 返回元组 ('url','www.baidu.com')
print a #输出 {'title': 'baidu', 'spam': 0}

#dic.setdefault()
a.clear()
print a.setdefault('name') # None
print a.setdefault('sex', 'N/A') # N/A
print a.setdefault('age', 'N/A') # N/A
print a # {'age': 'N/A', 'name': None, 'sex': 'N/A'}
print a.setdefault('age', 20) # N/A (由于前面已经设置了age默认值，字典中已存在age项，所以在这里在设置会返回已有的键对应的值，并且不会更新字典的键值)
print a # {'age': 'N/A', 'name': None, 'sex': 'N/A'} (age键对应的值没有被上一步的setdefault操作修改)
a['a'] = 'abc'
a['sex'] = 'boy'
a['age'] = 21
print a # {'a': 'abc', 'age': 21, 'name': None, 'sex': 'boy'}

#dic.update()
a.clear()
a['name'] = 'shj'
a['sex'] = 'boy'
print a # {'name': 'shj', 'sex': 'boy'}
b = {'name':'abc', 'age':20}
a.update(b)
print a # {'age': 20, 'name': 'abc', 'sex': 'boy'}
c = {'stature':170}
#可以使用dict类的update(旧字典，新字典)函数
dict.update(a, c)
print a, c #{'age': 20, 'stature': 170, 'name': 'abc', 'sex': 'boy'} {'stature': 170}











#------------------------------------- 第五章 ------------------------------------#


'''

    序列解包 （变量赋值）

        * 左侧变量个数 =  右侧值的个数 (x, y, z = 1, 2, 3)

            - x, y, z = 1, 2 或 x, y = 1, 2, 3 都会引发异常
'''


x, y, z = 1, 2, 3
print x, y, z

values = 4, 5, 6
print values # (4, 5, 6)
x, y, z = values
print x, y, z

x, y = y, x
print x, y

people = {'name': 'shihongji', 'age':30}
key, value = people.popitem() # popitem() 方法会返回元组
print key, value


x = y = 1
print x, y
# 同
y = 1
x = y
print x, y



'''

    布尔类型（Boolean）

        * False None 0 "" () [] {} 作为布尔表达式时，都被解释器看做False
        
'''


print True == 1 # True
print False == 0 # True
print True + False + 42 # 43



'''

    bool() 类型转换
    
'''

print bool(1) # True
print bool(0) # False
print bool(0.0) # False
print bool("") # False
print bool(()) # False
print bool([]) # False
print bool(None) # False
print bool({}) # False


'''

    if 表达式：
        语句
    elif 表达式:
        语句
    else 表达式：
        语句

'''

a = 1

if a > 0:
    print 'a > 0'
elif a < 0:
    print 'a < 0'
else:
    print 'a == 0'


'''

    比较运算符

        * ==、 <、 >、 >=、 <=、 !=
        * x or y (类似于AS中逻辑或运算符 || )
        * x and y (类似于AS中逻辑并且运算符 && )
        * not x  (类似于AS中逻辑非运算符 ！)
        * x is y (xy是同一个对象)
        * x is not y （xy不是同一个对象）
        * x in y (x 在 y中，例如之前列表用的 a = [1,2,3] print 1 in a)
        * x not in y (x 不在 y中)
        * x < > y  等同于 x != y 尽量避免使用x < > y这种方式，遇见能明白即可
        
'''


print 'alpha' < 'beta' # True
print [2,5] < [1,2] # False
print [2, [1, 2]] > [2, [1,6]] # False


'''

    三元运算符（条件运算符）

        * a if b else c (如果b为真，返回a，否则返回c)
        # a = b > 0 ? 1:2 (AS的写法)
'''

name = raw_input('Please Input Your Name:')
print 'OK' if name == 'shihongji' else 'Error'


'''

    assert 关键字 （目前不理解，日后慢慢看）

'''


'''

    循环遍历列表 for

        * 可以在循环中使用序列解包
'''

people = {'name':'shihongji', 'age':20}
for key in people:
    print key + ':' + str(people[key])


for key, value in people.items():
    print str(key), str(value)


# 打印名字对应年龄
names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]

# 方法一
for i in range(len(names)):
    print names[i], 'is', ages[i], 'years old'

# 方法二 使用内建函数 zip()
for name, age in zip(names, ages):
    print name, 'is', age, 'years old'


'''

    内建函数

        * zip() 把两个序列压缩在一起，返回一个元组的列表
            - 可以作用于任意多的序列
            - 可以应付不等长的序列，当最短序列用完的时候就会停止

        * enumerate() 返回索引-值对

'''

# zip()
print zip(names, ages) # [('anne', 12), ('beth', 45), ('george', 32), ('damon', 102)]

names.pop() # 移除names中的一个元素，使names和ages元素个数不等
print names
print zip(names, ages) # [('anne', 12), ('beth', 45), ('george', 32)]

# enumerate()
for index, name in enumerate(names):
    print 'names[', index, '] = ', name


'''

    while True/break语句
    


word = raw_input('Please enter a word:')
while word:
    print 'The word was ' + word
    word = raw_input('Please enter a word:')

# 由于上面的写法有重复的代码 word = raw_input('Please enter a word:')
# 此时可以使用 while True/break语句

while True:
    word = raw_input('Please enter a word:')
    if not word:
        break
    print 'The word was ' + word

'''

'''

    for 循环 搭配else

        * 当迭代的对象迭代完并为空时，位于else的子句将执行
        * 如果在for循环中含有break时则直接终止循环，则不会执行else子句

        如：从0-9中查找数字5，找到就停止循环，找不到就提示没找到
'''

# 方法一 常用做法要设置一个是否找到的标识符
founded = False

for num in range(10):
    if num == 5:
        print 'found it! num = %s' % num
        founded = True
        break;
if not founded:
    print 'not found it ...'

# 方法二 使用for循环搭配else
for i in range(10):
    if i == 5:
        print 'found it! i = %s' % i
else:
    print 'not found it ...'

# 期望结果是：found it! i = 5
# 实际结果是：found it! i = 5 not found it ... (else 条件后的语句也输出了)
# 正确的写法应该为：
for i in range(10):
    if i == 5:
        print 'found it! i = %s' % i
        break # 此处break很重要
else:
    print 'not found it ...'



'''

    列表推导式

        利用其他列表创建新列表的一种方法，工作方式类似于for循环

'''

print [x * x for x in range(10)] # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 同

l = []
for x in range(10):
    l.append(x * x)

print l # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print [x * x for x in range(10) if x % 3 == 0] # [0, 9, 36, 81]

# 同

l = []
for x in range(10):
    if x % 3 == 0:
        l.append(x * x)

print l # [0, 9, 36, 81]



'''

    pass、del、exec、eval语句

        * del
            - 删除变量对数据的引用，并且删除此变量，
            - 如果没有变量引用此数据，还会触发垃圾回收内存
'''

x = 1
print x # 1
del x
# print x # NameError: name 'x' is not defined








#------------------------------------- 第六章 ------------------------------------#


'''

    函数定义

        * 语法：def func():

    函数参数
    
        * 语法：def func(x, y, z = 1, *tupleArgs, **dicArgs1)
            - *tupleArgs是元组数据
            - **dicArgs1是字典数据

'''


def func(x, y=5, *a, **b):
    print x, y, a, b

func(1) # 1 5 () {}
func(1,2) # 1 2 () {}
func(1,2,3) # 1 2 (3,) {}
func(1,2,3,4) # 1 2 (3, 4) {}
func(x=1) # 1 5 () {}
func(x=1,y=1) # 1 1 () {}
func(x=1,y=1,a=1) # 1 1 () {'a': 1}
func(y=2,x=1,a=1,b=1) # 1 2 () {'a': 1, 'b': 1}
func(1,y=1) # 1 1 () {}
func(1,2,3,4,a=1) # 1 2 (3, 4) {'a': 1}
func(1,2,3,4,k=1,t=2,o=3) # 1 2 (3, 4) {'k': 1, 't': 2, 'o': 3}



'''

    参数反转
        将参数收集为元组和字典上面用过，但事实上，如果使用*和**的话，可以执行反操作
        
'''

# 使用*号运算符
def add(x, y): return x + y

params = (1, 2)
print add(*params) # 3

# 使用**运算符
def hello(name = 'shihongji', greeting = 'Hello'):
    print greeting, name

params = {'name':'hongji', 'greeting':'Well met'}
hello(**params)


def with_star(**kwds):
    print kwds['name'], 'is', kwds['age'], 'years old'

def without_stars(kwds):
     print kwds['name'], 'is', kwds['age'], 'years old'

args = {'name':'shihongji', 'age':20}
with_star(**args)
without_stars(args)


'''

    使用拼接操作符传递参数 （目前不是很清楚，待日后补充）

        * 这种方式可以不用关心参数的个数，在调用超类的构造函数时这个方法尤其有用

'''

def foo(x, y, z, m = 0, n = 0):
    print x, y, z, m, n


def call_foo(*args, **kwds):
    print 'Calling foo!'
    foo(*args, **kwds)




'''

    函数注释

        * 使用#
        * 使用文档字符串
            - 在函数的开头写字符串，它会作为函数的一部分进行存储
            - 文档字符串的访问方式 func.__doc__
'''


def func(x):
    'This is a func'
    return x

print func(1) # 1

print func.__doc__ # This is a func



'''

    vars()函数

        * 变量和所对应的值是个不可见的字典，vars()函数可以返回该字典
        
'''

ccc = 1

dic = vars()
print dic
print dic['ccc'] # 



'''

    globals()函数
        * 返回全局变量的字典
        * 如果局部变量或参数的名字和想要访问的全局变量名相同的话，
            可以使用globals()函数获取全局变量值

    
'''

parameter = 'berry'

def combin(parameter):
    print parameter , globals()['parameter']

combin('Shrub') # Shrub berry



'''
    代码段一会出现 local variable 'x' referenced before assignment 的异常

    原因：
        Python中如果在函数内部给全局变量赋值，那该变量会自动转为局部变量
        如本段代码中 x = x + 1:
        在函数内给全局变量x赋值，导致变量x自动转为了局部变量
        x + 1中x变量还没有被声明就开始使用，所以会报错

    解决：
        使用global在函数中声明x是全局变量如：代码段二

'''

# 代码段一

'''
x = 1
def add():
    x = x + 1
    print x
add()
print x

'''

# 代码段二

x = 1
def abcd():
    global x
    x = x + 1
    print x # 2

print x # 1
abcd()
print x # 2



'''

    嵌套作用域

        * Python中函数可以嵌套
        * 在需要用一个函数创建另一个函数时使用
        * 外层函数返回里层函数
        * 返回的函数还可以访问他定义所在的作用域（它带着它的相关环境和先关局部变量）
        * 每次调用外层函数，它内部的函数都会被重新定义

'''


def mul(factor):
    def mulByFactor(number):
        print factor * number
    return mulByFactor # 返回里层函数mulByFactor


mbf = mul(5)
print type(mbf)
mbf(5) # 25

mul(10)(2) # 20 





#------------------------------------- 第七章 ------------------------------------#

'''

    面向对象编程（OOP）

        * 类定义
            - 语法：class 类名:

'''



class Animal:

    def __init__(self):
        self.__animalType = '动物'
    
    def setName(this, name):
        this.name = name

    def getName(this):
        return this.name

    def greet(this):
        print 'I\'m %s' % this.name

    def run(self):
        print 'Animal run!'

    def eat():
        print self.__animalType

cat = Animal()
dog = Animal()
cat.setName('P1')
dog.setName('P2')
cat.greet() # I'm cat
dog.greet() # I'm dog
print cat.name # cat

cat.name = 'cat1'
cat.greet() # I'm cat1

cat.age = 2
print cat.age # 2



'''

    继承和多态

        * 类继承
            - 语法：class 类名(父类):

        *当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，
        在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态。

    重写（覆盖）：

        子类中的方法名同父类中的方法名一样（参数一不一致无所谓）
    
'''


# 子类中没有run()方法
class Cat(Animal):
    pass

class Dog(Animal):
    pass

cat = Cat()
dog = Dog()
cat.run() # Animal run!
dog.run() # Animal run!


# 给子类添加跟父类一样的run()方法，此时子类和父类存在相同的run()方法
class Cat1(Animal):
    '方法覆盖'
    def run(self):
        print 'Cat run!'

class Dog1(Animal):
    '方法覆盖'
    def run(self):
        print 'Dog run!'

cat = Cat1()
dog = Dog1()
cat.run() # Cat run!
dog.run() # Dog run!


'''

    子类不能继承父类的私有属性和方法

'''

class Monkey(Animal):

    # 爬树
    def climbTree():
        print 'monkey Climb Tree...'


m = Monkey()

# 在eat()方法中打印__animalType，由于子类不能继承父类私有属性
#，但是在子类中又没有 __animalType 这个属性，所以会报错

# m.eat() 结果： TypeError: eat() takes no arguments (1 given)


'''
    * 多态的好处就是，当我们需要传入Dog、Cat……时，我们只需要接收Animal类型就可以了，
    * 因为Dog、Cat……都是Animal类型，然后，按照Animal类型进行操作即可。
    * 由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，
    * 就会自动调用实际类型的run()方法，这就是多态的意思：


    * 对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，
    * 就可以放心地调用run()方法，而具体调用的run()方法是作用在Animal、Dog还是Cat对象上，
    * 由运行时该对象的确切类型决定，这就是多态真正的威力：调用方只管调用，不管细节，
    * 而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。
    * 这就是著名的“开闭”原则：

        - 对扩展开放：允许新增Animal子类；

        - 对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。

'''

def run_twice(Animial):
    Animial.run()
    Animial.run()
    print

run_twice(Cat1()) # Cat run! Cat run!
run_twice(Dog1()) # Dog run! Dog run!


'''

    __new__()：

        * 对象创建时首先调用 __new__() 构造函数生成对象，
        然后调用__init__(self)函数初始化数据

    初始化函数 ： __init__(self)

        * 有了__init__方法，在创建实例的时候，就不能传入空的参数了，
        * 必须传入与__init__方法匹配的参数，但self不需要传

    私有变量 ： __变量名 （左侧是双下划线）

    私有变量访问方式：

        * 给私有变量添加对外的get和set方法
        * 如：变量__sex
        * set_sex(self, value) 和 get_sex(self)



    私有函数： __函数名() (同私有变量一样都是以双下划綫开头)
    
'''


class Student():
    def __init__(self, name, score, sex):
        self.name = name
        self.score = score
        self.__sex = sex

    def set_sex1(self, sex):
        self.__sex = sex

    def get_sex(self):
        return self.__sex

    def __sayHello(self):
        print('sayHello')

    def print_studentInfo(self):      
        print '%s is a %s, thie score is : %s' % (self.name, self.__sex, self.score)

stu = Student('xiaoming', '59', 'boy')
stu.print_studentInfo() # xiaoming : 59

stu.set_sex1('girl') # 在这里sex是私有变量 不能再使用stu.__sex方式进行赋值
stu.print_studentInfo()

# stu.__sayHello() 外部是不能调用私有函数的

print stu.get_sex()



'''

    __str__(self):

        * 用来打印对象信息

        * 一定要有返回值

'''

class Car():

    def __init__(self, name, color):
        self.name = name
        self.color = color

    # 重写 __str__(self)
    
    def __str__(self):
        return 'name : %s, color : %s' % (self.name, self.color)
        

car = Car('奥拓', '白色')

# 如果不想看到这样的结果(内存地址)：<__main__.Car instance at 0x02822580>

# 就重写 __str__(self) 结果： name : 奥拓, color : 白色

print(car) 



'''

    设置、获取对象属性和检测对象某属性是否存在
    
        * hasattr()
        * setattr()
        * getattr()

'''

print hasattr(stu, 'height') # False
setattr(stu, 'height', '170') 
print stu.height # 170
print getattr(stu, 'height') #170




'''

    获取对相关信息

        * type()
        * isinstance()
        * dir()
            - 获得一个对象的所有属性和方法，它返回一个包含字符串的list
        * issubclass(父类， 子类)
            - 检查一个类是不是另一个类的子类

'''


print type('123') # <type 'str'>
print type(cat) # <type 'instance'>
print type(dog) # <type 'instance'>
print type(Animal) # <type 'classobj'>
print isinstance(cat, Cat) # False
print isinstance(cat, Animal) # True
print dir(Animal) # ['__doc__', '__module__', 'getName', 'greet', 'run', 'setName']
print Cat1.__doc__ # 方法覆盖
print issubclass(Cat1, Animal) # True
print issubclass(Animal, Cat1) # False



'''

    给类的实例动态绑定属性和方法

'''

# 交通工具类
class vehicle:
    pass

ve = vehicle()
ve.speed = 100 # 动态绑定speed属性
print ve.speed # 100

# 定义类外的一个方法
def run(self):
    print 'running'

# 给实例ve绑定run方法
from types import MethodType
ve.run = MethodType(run, ve, vehicle)
ve.run()



'''


    使用__slots__

        * 定义类的时候定义一个特殊的__slots__变量，用来限制该类能添加的属性,
        相当于java，c++中的成员变量声明
            - 比如：只允许对vehicle2类实例添加speed和color属性

        * __slots__核心作用是：可以在创建大量实例的时候更加节省内存。
    
'''


# 经测试，类要继承object 使用__slots__才会生效
class vehicle2(object):
    __slots__ = ('speed', 'color')


ve2 = vehicle2()
ve2.speed = 100
ve2.color = 'white'
print ve2.speed # 100
print ve2.color # white
# ve2.price = 2780 # AttributeError: 'vehice2' object has no attribute 'price'

#__slots__定义的属性仅对当前类起作用，对继承的子类是不起作用
#car类虽然继承了vehicle2类，但是没有使用__slots__属性，所以car的实例可以绑定price属性
class car(vehicle2):
    pass

c = car()
c.price = 2000
print 'car\'s price is:', c.price # car's price is: 2000



# 除非在子类中也定义__slots__，这样，子类允许定义的属性就是自身的__slots__加上父类的__slots__
class bike(vehicle2):
    __slots__ = ('name', 'price')


b = bike()
b.price = 1000
b.name = 'dasanba'
b.speed = 100
b.color = 'black'
print b.price, b.name, b.speed, b.color # 1000 dasanba 100 black
# b.size = 1890 # AttributeError: 'bike' object has no attribute 'size'




'''

    使用@property

        * Python内置的@property装饰器就是负责把一个方法变成属性调用的
'''


# 正常调用属性赋值和取值的方式
class point:
    def set_x(self, x):
        self.x = x

    def get_x(self):
        return self.x

p = point()
p.set_x(10)
print 'X:', p.get_x() # X:10


# 使用@property的方式
class point2:
    
    @property
    def x(slef):
        return self.x    

    @x.setter
    def x(self, x):
        self.x = x

p2 = point2()
p2.x = 20
print 'p2.x :', p2.x # p2.x : 20



'''

    多重继承

        * 语法：class 类名(父类，类Mixin...)

        * 通过多重继承，一个子类就可以同时获得多个父类的所有功能。


    Mixin设计

        * 表示混入(mix-in)，它告诉别人，这个类是作为功能添加到子类中，而不是作为父类

    使用Mixin类实现多重继承要非常小心
    
        * 首先它必须表示某一种功能，而不是某个物品，如同Java中的Runnable，Callable等
        * 其次它必须责任单一，如果有多个功能，那就写多个Mixin类
        * 然后，它不依赖于子类的实现
        * 最后，子类即便没有继承这个Mixin类，也照样可以工作，就是缺少了某个功能。

    下面的Airplane类实现了多继承，不过它继承的第二个类我们起名为PlaneMixin，
    而不是Plane，这个并不影响功能，但是会告诉后来读代码的人，这个类是一个Mixin类。
    所以从含义上理解，Airplane只是一个Vehicle，不是一个Plane。
'''

class Vehicle(object):
    pass
 
class PlaneMixin(object):
    def fly(self):
        print 'I am flying'
 
class Airplane(Vehicle, PlaneMixin):
    pass



'''

    Python中还有一个定制类和元类的概念（暂不明白，日后补充）

'''





#------------------------------------- 第八章 ------------------------------------#


'''

    异常
        语法：
        
            try:
                pass
            except:
                pass
            finally:
                pass

    Python所有的错误都是从BaseException类派生的，常见的错误类型和继承关系看这里：
    https://docs.python.org/2/library/exceptions.html#exception-hierarchy

    
'''


try:
    print 10 / 0
except Exception, e:
    print e
finally:
    print 'finally...'


'''

    如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出。

    如下面实例：

    def foo(s):
        return 10 / int(s)

    def bar(s):
        return foo(s) * 2

    def main():
        bar('0')


    main()


'''




'''

    记录错误

        * Python内置的logging模块可以非常容易地记录错误信息

        * 通过配置，logging还可以把错误记录到日志文件里

        

    下面代码段同样是出错，但程序打印完错误信息后会继续执行，并正常退出：

'''

import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except StandardError, e:
        logging.exception(e)

main()
print 'END'



'''

    自定义异常类

        语法：
            class CustomException(Exception): pass
            
        * 向其他类一样，只要确保从Exception类继承（不管是间接还是直接的，就是说继承其他的内建异常类也可以）

'''


'''

    多个Except

'''

try:
    x = input('Enter the first number: ')
    y = input('Enter the second number: ')
    print  x / y

except ZeroDivisionError:
    print 'ZeroDivisionError...'

except TypeError:
    print 'TypeError...'

# 或

except (ZeroDivisionError, TypeError):
    print 'Error Message...'


'''

    获取异常的对象e

'''
try:
    print 1 / 0

except (ZeroDivisionError, TypeError), e:
    print 'Error Message: ', e




'''

    给try/except添加else语句

        语法：
            try:
            except:
            else:
            finally:

        * else中的语句只有在没有异常发生的时候才会执行

        如下示例：

            * 输入不正确会引异常，程序就会不断要求输入
            * 输入正确没有异常，就会执行else中的语句，结束程序

'''


while True:
    try:
        x = input('Enter the first number: ')
        y = input('Enter the second number: ')
        print  x / y
        
    except:
        print 'Invalid input,please try again!'

    else:
        break

    finally:
        print 'exec finally...'


'''

    raise关键字

        * 将异常抛向上层调用处

'''

def cacl():
    try:
        print 1 / 0
    
    except:
        raise Exception('Something is wrong!') # 从此处抛出异常到标记二处



def exec_cacl():
    cacl() # 标记二 此处将异常继续外抛至标记三处


# exec_cacl() # 标记三 此处异常未做处理，程序强制终止

# 下面代码给调用exec_cacl函数添加了异常捕捉优化处理
# 程序捕捉到异常后，会继续向下执行，不会强制终止程序
try:
    exec_cacl()

except Exception, e:
    print 'exec_cacl errorInfo: ', e


print 'END!'







#------------------------------------- 第九章 ------------------------------------#


'''

    绑定方法和未绑定方法

        * 类里面的方法就是非绑定方法（用类名调用方法），实例里面的方法就是绑定的（用类的实例调用方法）

        参考：http://blog.csdn.net/qin_shang_/article/details/79013420


    调用超类的非绑定方法

        * parents.__init__(this) (可以使用)
        
        * super(child1, this).__init__() (推荐使用)

        super()详细参考：
        http://blog.csdn.net/mashijia986/article/details/79126287
'''


from random import randint

class parents(object):
    def __init__(this):
        this.xx = randint(1,10)
        this.yy = randint(1,10)

    def cacl(this):
        print 'x / y = %.1f' % (this.xx / this.yy)

    def printString(this):
        print 'printString...'

class child(parents):
    def __init__(this):
        pass

# 父类实例直接调用cacl方法没有问题
p = parents()
p.cacl() # x / y = 1.0

# 子类实例调用父类中的方法
c = child()
c.printString() # printString...

# 因为cacl方法中使用到xx和yy类属性，但是在子类调用cacl方法时，父类没有被初始化，
# 所以变量xx和yy变量没有被创建
# 解决办法： 调用未绑定的父类方法
try:
    c.cacl() 
except Exception, e:
    print e # AttributeError: 'child' object has no attribute 'xx'
 

# 解决上面代码报错问题：   调用未绑定的父类方法

class child1(parents):
    def __init__(this):
        
       # parents.__init__(this) # 可以使用这种方法
       
       # 或使用
       
       super(child1, this).__init__() # 推荐使用这种方法

c1 = child1()
c1.cacl() # x / y = 1.0





'''

    静态方法和类成员方法

        * 静态方法和类成员方法在创建时分别被装入Stticmethod类型和Classmethod类型的对象中

    静态方法

        * staticmethod

        * 不需要self参数，可以被类本身直接调用


    类成员方法

        * classmethod

        * 方法在定义的时候需要名为cls的类似于self的参数


    装饰器

        * 使用@操作符

        * @staticmethod  @classmethod

    
'''


class MyClass:

    @staticmethod
    def smeth():
        print 'This is a static method'

    @classmethod
    def cmeth(cls):
        print 'This is a class method of', cls


MyClass.smeth()

# 类成员方法可以直接用类的具体对象调用，但cls参数是自动被绑定到类的
# 所以一可直接使用 MyClass.cmeth()
MyClass.cmeth()


'''

    生成器暂不了解

'''




#------------------------------------- 第十章 ------------------------------------#



'''

    模块定义

        * 为了代码码重用

    假设现在有一个hello.py的文件，保存在e:/PythonSpace目录下

    下面代码是告诉解释器在哪里找模块
    
'''

import sys
sys.path.append('e:/PythonSpace')

'''

    导入模块

        * 导入模块多次和导入一次效果是一样的
    
'''


import HellloWorld


'''

     模块重新加载 ： 尽可能避免重新载入

        * reload(模块名)

'''

# hello模块已经被导入了一次，这里通过reload函数的返回值付给hello
# 重新载入的版本替换了上一次导入的版本
HellloWorld = reload(HellloWorld)


'''

    __name__变量
    
        * 在主程序(当前执行的程序)中使用时，__name__的值是'__main__'
        * 如果是导入的模块，这个值就被设定为模块的名字
'''

print __name__ # '__main__'

print HellloWorld.__name__ # HellloWorld

print sys.path

from Hello2 import hello
hello()


import drawing
from drawing import color

color.test()

print range.__doc__


'''

    标准库

        * Python中包括了一些模块，总称为标准库

        * 简单介绍一部分

            - sys 通过该模块可以访问多个和Python解释器联紧密的变量和函数

            - os 通过该模块可以访问到多个和操作系统联系紧密的变量和函数

            - fileiput 通过该模块可以轻松遍历多个文件和流中的所有行

            - sets、heapq和deque 这三个模块提供了3个有用的数据结构。
                . 集合也以内建的类型set存在

            - time 通过该模块可以获取当前时间， 并可以进行时间日期操作和格式化

            - random 该模块中的函数可以产生随机数、从序列中选取随机元素以及打乱列表元素

            - shelve 创建持续性映射，同时将映射的内容保存在给定文件名的数据库中

            - re 支持正则表达式模块
    
'''



#------------------------------------- 第十一章 ------------------------------------#



'''

    文件读写

        open函数

            * open(name[, mode[, buffering]])
'''

help(open)

print open.__doc__

f = open('somefile.txt', 'w')

# 每次调用f.write()的时候，数据都会以追加的方式写入文件中
f.write('Hello')
f.write('World')

f.close()


f = open('somefile.txt', 'r')

# 读5个字节的字符
print f.read(5) # Hello

# 读取剩余的字符
print f.read() # World

f.close()


'''
    read([bytes])

        * 可以指定读取的字节数

        * 从文件指针所在的位置，读到文件结尾(或读到所指定的字节数)

    readline([bytes]) - 读取一行

        * 可以指定读取的字节数

        * 从文件指针所在位置一直到换行符出现（会连同换行符一起读出）

    readlines() - 读取文件中的所有行，并且将其作为列表返回
    

    writelines(列表) - 向文件中写入多行数据

        * 同readlines()相反，参数是一个字符串列表

        * 没有writeline()方法，只能使用write

'''


f = open('somefile.txt', 'w');
f.write("hello shihongji\n")
f.write('hello shihonghong')
f.close()

f = open('somefile.txt', 'r')
print f.read() # hello shihongjihello shihonghong 读取文件中所有文本
print f.readline() #由于执行了f.read(),此时指针已经处于文件末尾,所以不能读取出文本
f.seek(0) # 把指针指回文件开头
print  f.readline(5) # hello 读取5个字节
print  f.readline() #  shihongji
print f.readlines() # ['hello shihonghong'] 在当前游标的位置读取
f.seek(0)
print f.readlines() # ['hello shihongji\n', 'hello shihonghong']

f.close()

f = open('somefile.txt', 'w')
f.writelines(["write", "lines"])
f.close()

raw_input("123") # 通过等待输入来让程序暂停, 查看文件中的内容

'''

    管道输出

        * sys.stdout 标准输出, 对应的操作就是print（打印）

            - print 1
            
            - 其效果是把 1 写在console（命令行）里面让你看
            - 实际上他的操作可以理解为：把console（命令行）作为一个板子，
            通过sys.stdout = console指定往console板子上写东西(console 是默认的，
            也就是说你不修改要往哪儿写的话，就会默认往这写)，在print 1的时候，
            就是告诉python，我要写1，然后python就会去sys.stdout所指定的板子里，
            也就是console（命令行）里写上 1。
            -（标准错误输出也是同样的过程，你会发现当程序出错时，错误信息也会打印在console里面。
            - 其实只要一个对象具有write方法，就可以被当作“板子”，告诉sys.stdout去哪里写。
            - 说道write方法，第一个想到的可能就是文件操作了

            
        
        * sys.stdin 标准输入， 则对应input（接收输入）操作

            - 逻辑同sys.stdout一样，默认的板子都是concole(命令行)
            - 只要一个对象具有write方法，就可以被当作“板子”，告诉sys.stdout去哪里读。

        * sys.stderr 标准错误输出， 和标准输出类似也是print（打印）


        参考 http://www.cnblogs.com/turtle-fly/p/3280519.html
        
'''


import sys

# 此文件对象有write()方法，就可以被用来当做标准输出和标准错误输出的板子
f = open('somefile.txt', 'w')
__console__ = sys.stdout # 把默认的板子（命令行）做一个备份，以便再改回来

sys.stdout = f

print 123456789 # 输出到文件里

f.close() # 一定要记得关闭文件

sys.stdout = __console__ # 把板子重新换成console(控制台)

print 2 # 输出到控制台






'''

    sys.stdin.read() & sys.stdin.readline()

        * sys.stdin 往板子上写内容

        * sys.stdin.read() & sys.stdin.readline() 把写在板子上的内容读出来

        * sys.stdin.read()可以接受多行的标准输入,读取数据 ctrl+d是结束输入 ，enter是换行。

        * sys.stdin.readline() 仅仅接受一行的全部输入,会将标准输入全部获取，
            包括末尾的'\n'，因此用len计算长度时是把换行符'\n'算进去了的

    raw_input 和 sys.stdin.readline()区别
    
        * raw_input()获取输入时返回的结果是不包含末尾的换行符'\n'的

        * sys.stdin.readline() 读取的结果中包含末尾的换行符'\n'


    strip('\n')

        * 去掉读取结果后面的换行符 sys.stdin.readline().strip('\n')
    
'''

text = sys.stdin.read()
print 'sys.stdin.read: ', text


text = sys.stdin.readline()
print 'sys.stdin.readline = ', text


text1 = sys.stdin.readline()
print 'sys.stdin.readline.len = ', len(text1)


text2 = sys.stdin.readline().strip('\n')
print 'sys.stdin.readline.strip.len = ', len(text2)


'''

    seek(offset[, whence])

        * 方法用于移动文件读取指针到指定位置。

        * offset -- 开始的偏移量，也就是代表需要移动偏移的字节数

        * whence：
            - 给offset参数一个定义，表示要从哪个位置开始偏移
            - 可选，默认值为 0
            - 0代表从文件开头开始算起
            - 1代表从当前位置开始算起
            - 2代表从文件末尾算起

            
    tell()

        * 方法返回文件的当前位置，即文件指针当前位置

'''

x =file('a.txt','w+')
x.write('aaaaaaaaaa') # 在文件里写10个a

print x.tell()      # 10 显示表明当前游标在文件末尾

x.seek(3)    # 移动3个字节，whence没有设置默认为从文件开头开始
print x.tell() # 3

x.seek(5,1)  # 移动5个字节，1代表从当前位置开始
print x.tell() # 8 从当前游标所在位置移动5个字节

x.seek(-1,2)# 向前移动1个字节，2代表从文件末尾开始
print x.tell()

print x.readline() # a


'''

    f.flush()

        * 当数据存储在缓存中，直到关闭文件才会被写到文件，如果还要继续使用文件（不关闭文件）
            - 有想更细文件内容，调用flush()方法，吧缓存中的数据写入文件中

'''



'''

    fileinput() - 迭代大文件时使用

        * 使用时需要导入fileinput模块

        * fileinput.input(filename)该模块的input()函数同readlines()函数类似，
            但是input()每次只生成一行迭代对象
'''

import fileinput

for line in fileinput.input('a.txt'):
    print line






