# -*- coding:utf-8 -*-
''''''

'''

贪婪模式：

    * 总是尝试匹配尽可能多的字符
    * Python中的正则表达式的数量词（*、+、？、{N}、{M,N}）默认是贪婪的


非贪婪模式：

    * 总是尝试匹配尽可能少的字符
    
    
贪婪变非贪婪：

    * 在数量词（*、+、？、{N}、{M,N}）后面加上 '?'
    
    * 例：
        
        1、匹配数字一次或多次：reFunc('aa\d+', 'aa123456bbb')
            输出： aa123456
            
        2、例一基础上使用贪婪模式：reFunc('aa\d+?', 'aa123456bbb')
            输出： aa1  （一次或多次，尽可能少的去匹配数字，所以只匹配了一次）
            

贪婪变非贪婪模式无效情况：

    * 例：
        
        1、reFunc('aa\d+?bb', 'aa123456bbb')
            输出：aa123456bb 
            （因为 表达式限定了 前面有 'aa' 后边有 'bb'，所以中间的123456全部匹配到）

'''

import re

def reFunc(restr,* args):

    for s in args:
        print(restr + ', ' + s)
        res = re.match(restr ,s)
        if res is not None:
            print 're result：' + res.group()
        else:
            print('result is None')

reFunc('aa\d+?bb', 'aa123456bbb')
