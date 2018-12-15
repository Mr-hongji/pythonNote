'''

    遍历

        * for ...in 可以遍历字符串的每个字符

'''


word = 'helloshihongji'

for w in word:
    print w,

print



'''

    索引访问

        * 通过索引访问字符串中的某个字符串
        * 与List不同的是，字符串不能通过索引访问去更改其中的字符

'''


print word[0] #输出第一个字符 h

print word[1] #输出第二个字符 e 

print word[-2] #输出倒数第二个字符 j

# word[1] = 'a' 的赋值是错误的, 字符串不能通过索引访问去更改其中的字符



'''

    切片

        * 具体规则同List一致
    
'''


print word[1:5]

print word[:5]

print word[0:]

print word[:]




'''

    连接字符串

        * join()
        * 用连接符把字符串中的每个字符重新连接成一个新字符串
        * 似乎没什么卵用
'''


separator = ', '

print separator.join(word)
