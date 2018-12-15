# -*- coding:utf-8 -*-
''''''

'''

列表（list）:
    
    * a = []
    
    * 有先后顺序
    
    * 有下标位[index]
    
    * 元素可以重复
    
    * 可变（可更新、删除）

'''

a = []

a = [1,2,3]

print a[1]

a.append(3) # 添加元素
print a

print a.pop() # 删除最后一个元素
print a


'''


元组（tuple）:

    * b = ()
    
    * 有先后顺序
    
    * 有下标位
    
    * 元素可以重复
    
    * 不可变（只能查询，不能添加、删除）
    

'''

b = ()
print b

b = (1,2,3)
print b

print b[1]



'''

字典（dict）

    * c = {key:value}
    
    * 没有先后顺序
    
    * 没有下标
    
    * key不可重复，value可重复
    
    * 可变

'''

c = {}

c = {'A':1}
print(c)

c['B'] = 'b'
print(c)

del c['A']
print(c)


'''

集合（set）
    
    * set是基本数据类型的一种集合类型,创建集合set、集合set添加、集合删除、
    交集、并集、差集的操作都是非常实用的方法
    
    * d = set()
    
    * 没有先后顺序
    
    * 没有下标
    
    * 不可重复
    
    * 可变（可增加、删除）

'''

# 创建集合 set

d = set('boy')
print(d) # set(['y', 'b', 'o'])

# 添加、更新、删除

d.add('python')
print(d) # set(['y', 'python', 'b', 'o'])

# 集合update方法：是把要传入的元素拆分，做为个体传入到集合中
d.update('python')
print(d) # set(['b', 'python', 'h', 'o', 'n', 'p', 't', 'y'])

d.add('user')
print(d) # set(['b', 'python', 'h', 'o', 'n', 'p', 't', 'y', 'user'])

d.remove('user')
print(d) # set(['b', 'python', 'h', 'o', 'n', 'p', 't', 'y'])

# 集合中的元素不能重复
d.add('python')
print(d) # set(['b', 'python', 'h', 'o', 'n', 'p', 't', 'y'])


'''

set() 集合操作符号

    * '-' 差集，相对补集
    * '&' 交集
    * '|' 合集、并集
    * '!=' 不等于
    * '==' 等于
    * 'in' 是成员关系
    * 'not in' 不是成员关系

'''

e = set('abc')
f = set('cdef')

# 交集
print(e & f) # set(['c'])

# 并集
print(e | f) # set(['a', 'c', 'b', 'e', 'd', 'f'])

# f 集合的补集
print(e - f) # set(['a', 'b'])

# e 集合的补集
print(f - e) # set(['e', 'd', 'f'])




