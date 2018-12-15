# -*- coding:utf-8 -*-
''''''
'''

    列表推导公式：
    
        * 用来生成列表

'''

# 生成一个0-9 的列表
a = [ i for i in range(0,10)]
print(a) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

b = [x for x in range(0,2) for y in range(0,3)]
print(b) # [0, 0, 0, 1, 1, 1]

# d等同于下面代码：

c = []

for x in range(0, 2):
    for y in range(0, 3):
        c.append(x)

print(c) # [0, 0, 0, 1, 1, 1]


'''

    生成元组列表

'''

d = [(x,y) for x in range(0,2) for y in range(0,3)]
print(d) # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]

# 输出 0-9 之间的偶数
e = [x for x in range(0,10) if x % 2 == 0]
print(e) # [0, 2, 4, 6, 8]

# 等同于：

e = []
for x in range(0,10):
    if x % 2 == 0:
        e.append(x)

print(e) # [0, 2, 4, 6, 8]




