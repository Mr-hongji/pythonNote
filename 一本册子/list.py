'''

    List 

        * list有两类常用操作：索引(index)和切片(slice)
'''


l = range(1,10)

print l



l = [365, 'everyday', 0.618, True]

for i in l:
    print i




'''

    访问元素

        * list[index]
'''

print l[0]




'''

    添加元素

        * list.append(1024)
'''

print '\n添加元素前:'
print l

l.append(1024)

print '添加元素后:'
print l





'''

    修改元素
    
        * list[index] = value
'''

print '\n元素修改前:'
print l

l[0] = 123

print '元素修改后:'
print l




'''

    元素删除

        * del list[index]

'''



print '\n元素删除前:'
print l

del l[0]

print '元素删除后:'
print l




'''

    上面的元素访问、添加、修改、删除 都是索引（index）操作


    下面介绍的是切片（slice）操作：

        1、 print l[startIndex:endIndex]
            * 开始位置包含在切片中，而结束位置不包括。
            * 输出index = startIndex 到 index = endIndex - 1 范围的值

        2、 print l[:endIndex]
            * 不指定startIndex，切片就从第一个元素开始

        3、 print l[startIndex:]
            *  不指定endIndex，切片一直到最后一个结束元素

        4、print l[:]
            * 都不指定，则返回整个列表

'''


l = [365, 'everyday', 0.618, True]


print l[-1] #输出list中的最后一个元素

print l[-3] #输出list中倒数第三个元素

print l[1:3] #输出 index = 1 到 index = 3-1 的元素  

print l[:3] #输出 index = 0 到 index = 3-1 的元素

print l[1:] #输出 index = 1 到 列表最后一个元素

print l[:]  #输出列表所有元素





