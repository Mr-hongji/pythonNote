# -*- coding:utf-8 -*-
print 1
print 'Hello PyCharm'
x =[4, 6, 2, 1, 7, 9]

print x

y = {'a':1, 'b':2, 'c':3}

print 'a' in y
print 'd' in y

for i in y:
    print i

# 降序排列
def comp(x, y):
    if x < y:
        return 1
    elif x > y:
        return -1
    else:
        return 0

print range(1, 4)
l = range(1, 4)
l.sort(comp)
print l


flag = 0

if flag:
    print '123'

def a():
    if flag:
        return 1, 2, '3'
    else:
        return

l = a()
print l is None

f = open('d:/ak.txt', 'r')
scoreData = f.readlines()
f.close()

cl = range(1, 5)
cl.sort(reverse=True)
print(cl)


from multiprocessing import Process,Queue

print Process.__dict__

print("----------------------------------------------------")

print Queue.__doc__

from random import randrange

loops = (randrange(2,5) for x in xrange(randrange(3,7)))
for i in loops:
    print i


f = 1

def test():
    print f
    while True:
        global f
        f += 1
        print f
        break

test()

import re

m = re.match('(\d+)[a-z]+(\d+)', '123abc456')
print m.group()
print m.group(1)
print m.group(2)






'System Idle Process    0 Console  0  28 K'

r'([\w.]+(?: [\w.]+)*)\s\s+(\d+) \w+\s\s+\d+\s\s+([\d,]+ k)'



s = ' 提问：中堂东港城7号楼1栋架空层绿化树苗干枯，且垃圾太多  编号:194088  '
print()
print re.sub(' ', '2' , s)
print s.strip().split('：')[-1].split(':')[0]

print s.strip().split('：')[-1].split(':')[0].strip()
print s.strip().split('：')[-1].split(':')[1].strip()


s = '  网友：浪淘淘 发言时间：2018-08-14 15:19:03  '

for c in s.strip().split(' '):
    print(c)
