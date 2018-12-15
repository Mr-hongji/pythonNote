# -*- coding:utf-8 -*-
''''''


import re


'''

re.compile()
    
    * 编译正则表达式模式，返回一个对象的模式。（可以把那些常用的正则表达式编译成正则表达式对象，
    这样可以提高一点效率。）
    
    * 格式：

        re.compile(pattern,flags=0)
        
        pattern: 编译时用的表达式字符串。
        
        flags 编译标志位，用于修改正则表达式的匹配方式，如：是否区分大小写，多行匹配等。
        
            * 常用的flags有：
                
                - re.S(DOTALL) 使.匹配包括换行在内的所有字符
                - re.I（IGNORECASE）使匹配对大小写不敏感
                - re.L（LOCALE）做本地化识别（locale-aware)匹配，法语等
                - re.M(MULTILINE) 多行匹配，影响^和$
                - re.X(VERBOSE) 该标志通过给予更灵活的格式以便将正则表达式写得更易于理解
                - re.U 根据Unicode字符集解析字符，这个标志影响\w,\W,\b,\B 

'''

tt = "Tina is a good girl, she is cool, clever, and so on..."
rr = re.compile(r'\w*oo\w*')

# 查找所有包含'oo'的单词
print(rr.findall(tt))   # 输出 ['good', 'cool']







'''

re.match()

    * 从字符串的起始部分对模式进行匹配
    * 匹配成功，返回一个匹配对象。
    * 匹配失败，返回None

'''

def reMatch(restr,* args):

    for s in args:
        print(restr + ', ' + s)
        res = re.match(restr ,s)
        if res is not None:
            print 're result：' + res.group()
        else:
            print('result is None')

reMatch('foo','food on the table') # 输出 foo

# 输出 result is None
# 因为foo 不在被搜索字符串起始位置
reMatch('foo','fast food')


'''

re.search()

    * 字符串的任意位置对模式进行匹配第一次出现的匹配情况
    * search 函数不但会搜索模式在字符串中第一次出现的位置，而且严格的对字符串从左到右搜索
    * 匹配成功，返回一个匹配对象
    * 匹配失败，返回None

'''

def reSearch(restr,* args):

    for s in args:
        print(restr + ', ' + s)
        res = re.search(restr ,s)
        if res is not None:
            print 're result：' + res.group()
        else:
            print('result is None')


reSearch('foo','fast food') # 输出 foo
reSearch('foo','food on the table') # 输出 foo



'''

group() 和 groups()

    * 都是调用 match 和 search 函数 返回的对像的两个主要方法
    
    * group 返回完整的匹配结果，如果模式中有分组，同时返回全部子组的元组
    
    * groups 返回所有子组的元组
    
    * 如果模式中没有分组，则group返回整个匹配结果，groups返回空元组


'''

def reMatch1(restr,* args):

    for s in args:
        print(restr + ', ' + s)
        res = re.match(restr ,s)
        if res is not None:
            print res.groups()
            print 're result：' + res.group()
            # print 'res.groups(0) = ' + res.groups(0) + '\nres.groups(1) = ' + res.groups(1)

        else:
            print('result is None')


reMatch1('(\d{3})-(\d{3})', '010-010')

'''
执行结果： 
    ('010', '010')
    re result：010-010 
    res.group(1) = 010 
    res.group(2) = 010

'''

reMatch1('\d{3}-\d{3}', '010-010')

'''

执行结果：

    ()
    re result：010-010
    
    Traceback (most recent call last):
      File "E:/PythonSpace/Exercise/����/3��re ���÷���.py", line 100, in <module>
        reMatch1('\d{3}-\d{3}', '010-010')
      File "E:/PythonSpace/Exercise/����/3��re ���÷���.py", line 83, in reMatch1
        + res.group(1) + " \nres.group(2) = " + res.group(2)
    IndexError: no such group

    1、因为模式中没有分组，所以 print res.groups() 输出 ()
    
    2、模式中没有分组，res.group() 只返回完整匹配结果，所以
        res.group(1) 和 res.group(2) 时出异常
'''


'''

findall()

    * 返回模式匹配中全部的非重复的情况
    * 总是返回列表
    * 匹配成功，返回所有成功匹配部分（从左向右按顺序排列）
    * 匹配不成功，返回空列表

'''

print re.findall('car','cr') # 输出 []

print re.findall('car','car') # 输出 ['car']

print re.findall('car', 'scary') # 输出 ['car']

# 输出 ['car'，'car'，'car'，'car']
print re.findall('car', 'carry the barcardi to the car car')


'''

finditer() 迭代

    * 与 findall()函数类似，但是要更节省内存


'''

it = re.finditer('car\d', 'car1ry the barcar2di to the car3',re.I)

g = it.next()
print 'result: ',g.group() # 输出 result:  car1

it = re.finditer('car\d', 'car1ry the barcar2di to the car3',re.I)

for g in it :
    print 'result = ',g.group()

globals()
'''

执行结果：

    result =  car1
    result =  car2
    result =  car3
    
    
re.finditer('car\d', 'car1ry the barcar2di to the car3',re.I)
中的 re.I 是不区分大消息的匹配

'''




'''

使用 sub() 和 subn() 搜索与替换

    * 两个函数几乎一样，都是讲字符串中所有匹配正则表达式的部分进行某种形式的替换
    
    * 用来替换的部分通常是一个字符串，但也可能是一个函数，该函数返回一个用来替换的字符串
    
    * sub() 返回数据：替换后的字符串
    
    * subn() 返回数据： （替换后的字符串，替换总数）
     
'''

res = re.sub('[ab]', 'x', 'abcdef')
print res # 输出 xxcdef

res = re.subn('[ab]', 'x', 'abcdef')
print res # 输出 ('xxcdef', 2)

def abc():
    return '[ab]'

res = re.sub(abc(), 'x', 'abcdef')
print res # 输出 xxcdef

res = re.subn(abc(), 'x', 'abcdef')
print res # 输出 ('xxcdef', 2)




'''

使用 split() 分割字符串

    * 如果分隔符是使用正则模式，则 re.split() 和 str.split() 没有区别

'''

print re.split(' ', 'Hello World') # 输出 ['Hello', 'World']

# 同

print 'Hello World'.split(' ') # 输出 ['Hello', 'World']


DATA = (
    'Mountain View, CA 94040',
    'Sunnyvale, CA',
    'Los Altos, 94023',
    'Cupertino 95014',
    'Palo Alto CA',
)

for d in DATA:
    print re.split(', |(?= (?:\d{5}|[A-Z]{2})) ', d)


'''

运行结果 ：

    ['Mountain View', 'CA', '94040']
    ['Sunnyvale', 'CA']
    ['Los Altos', '94023']
    ['Cupertino', '95014']
    ['Palo Alto', 'CA']

'''
