'''

    打开文件

        语法：
            * file(param1, param2)
            * param1 文件名
            * param2 文件操作方式 可选值：(r: 读文件     w: 覆盖写入模式    a: 追加写入模式)
            * 文件名可以用文件的完整路径，也可以是相对路径
            * 不加参数时，file为你默认为'r'
            * 如果文件不存在，会自动创建文件
'''

data = 'new file content'

f = file('output.txt', 'w')


f.write(data)


f.close()



'''

    读出data.txt文件中的内容, 写入到output.txt文件中

'''


rf = file('data.txt')
rdata = rf.read()
rf.close()

wf = file('output.txt', 'w')
wf.write(rdata)
wf.close()




'''

    把用户输入的数据保存到文件中

'''


youInput = input()

wf1 = file('output.txt', 'w')
wf1.write(str(youInput))
wf1.close()
