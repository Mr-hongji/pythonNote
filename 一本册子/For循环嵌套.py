for i in range(0,5):
    print "*" #结果：垂直输出5个*
    

#如果想让这5个*在同一行，就在print语句后面加上逗号
    
for t in range(0,5):
    print "*", #结果：5个*在一行输出


print '\n----循环嵌套练习----\n'

'''
输出 5行5列矩阵
    *****
    *****
    *****
    *****
    *****

    print后面没有写任何东西，是起到换行的作用
'''

print '\n--------方法一------\n'

for i in range(0,5):
    for j in range(0,5):
        print "*",
    print       

print '\n--------方法二------\n'

for i in range(0,5):
    str = ''
    for j in range(0,5):
        str += "*"
    print str


'''
输出如下格式:

    *
    **
    ***
    ****
    *****

    print后面没有写任何东西，是起到换行的作用
'''

print '\n------换个样式吧----\n'

for i in range(0,5):
    for j in range(0,i + 1):
        print '*',
    print
