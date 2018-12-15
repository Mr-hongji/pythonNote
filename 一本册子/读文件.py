'''

    打开文件

        语法：
            * file(param1, param2)
            * param1 文件名
            * param2 文件操作方式 可选值：(r: 读文件     w: 覆盖写入模式    a: 追加写入模式)
            * 文件名可以用文件的完整路径，也可以是相对路径
            * 不加参数时，file为你默认为'r'
            * 读取的问价必须存在，否则会报异常

'''


f = file('data.txt') #打开文件 变量 f 保存了这个文件




'''

    读取文件内容

        语法：
            * f.read()
            * readline() #读取一行内容
            * readlines() #把内容按行读取至一个list中

'''


data = f.read() #变量 f 保存了这个文件，还需要去读取它的内容

print data



'''

    lineData = f.readline()
    
    print '\n readLine' + lineData + '\n'
    
'''




'''
linesData = f.readlines()

lineNum = 0

for d in linesData:
    lineNum += 1
    print '第 %s 行: ' % str(lineNum)
    print d
    #print '第 %s 行:' % str(lineNum) + d  #这么输出会有乱码不知为啥

'''





'''

    关闭文件

        语法：
            * f.close()
    
'''


f.close() #做完对文件的操作之后，记得用close()关闭文件，释放资源
