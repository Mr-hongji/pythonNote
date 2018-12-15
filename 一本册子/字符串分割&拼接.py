'''

    函数：

    * split() 把一个字符串分割成很多字符串组成的list
    * 默认是按照空白字符分割
    * 用时也会按照换行符\n, 制表符\t进行分割
    
'''


sentence = 'I am an Englist sentence'

print sentence.split() #默认空格分割 结果：['I', 'am', 'an', 'Englist', 'sentence']



'''
    结果：['Hi', ' I am the one', ' Bye', '']
    
    * 注意最后那个空字符串。每个'.'都会被作为分割符，
    * 即使它的后面没有其他字符，也会有一个空串被分割出来
    
'''

section = 'Hi. I am the one. Bye.'

print section.split('.') 





'''

    字符串拼接
    
    函数：

    * join() 把一个list中的所有字符串连接成一个字符串
    * 首先需要设置字符串的连接符（拼接的字符串的分隔符）
'''

separator = '' #字符串被无缝连接在一起

l = ['I', 'am', 'an', 'Englist', 'sentence']

print separator.join(l)


separator = ' ' #字符串被空格分割连接在一起

print separator.join(l)


separator = ', '

l = ['Java', 'C', 'C++', 'Python', 'JavaScript']

print separator.join(l)
