# -*- coding:utf-8 -*-
''''''


import re


'''

符号 (?:)
    
    * 匹配不用保存的分组
    
    * 例：
    
        匹配以 '.' 作为结尾的字符串，但这些匹配不会保存下来供后续使用
    
'''

res =  re.match('(?:\w+\.)', 'www.baidu.com')

print res.group() # 输出 www.


'''

符号(?#name)

    * 表示注释，所有内容都被忽略
    * 不做匹配，制作为注释

'''

res = re.match('(?#name)', 'name:shihongji')
print res.group()



'''

符号(?=.com)

    * 例：字符串跟着 '.com' 才做匹配操作，并不使用任何目标字符串
        
        'baidu' 后边跟着的是 '.com', 才会匹配进行匹配
'''

res = re.match('baidu(?=.com)', 'baidu.com')
print res.group() # 输出 baidu


res = re.match('baidu(?=.com)', 'baidu.cn')
print res # 输出 None  因为 baidu 后边跟的是 .cn 所以, 不执行模式匹配



'''

符号(?<=010-)

    * 例： 如果 字符前是 '010-', 才做匹配

'''

res = re.match('(?<=010-)\d+', '010-7833033')
# print res.group() 匹配不出结果， 暂不知原因


'''
符号(?!.net)

    * 例：如果字符串后不跟这个 '.net',才会做匹配
    
'''

res = re.match('baidu(?!.net)', 'baidu.com')
print res.group() # baidu

res = re.match('baidu(?!.net)', 'baidu.net')
print res # None


'''

符号(?<!)

    * 例： 如果字符串前不是 'www.',做匹配

'''

import re

#  使用 match 匹配不出结果
# 使用 findall 和 search 都可以
res = re.match('(?<!www\.)baidu', 'doc.baidu.com')
# print res.group() # 匹配不出结果， 暂不知原因


print re.findall('(?<!www\.)baidu', 'doc.baidu.com') # ['baidu']

print re.search('(?<!www\.)baidu', 'doc.baidu.com').group() # baidu

'''
符号(?(id/name)Y|N)

    * 如果分组所提供的 id 或者 name（分组别名）存在，就返回正则表达式的条件匹配 Y，
    如果不存在，就返回正则表达式的条件匹配 N
    
    * |N 是可选项

    * 例：
    
        1、(\d)abc(?(1)\d|abc)
            - (\d)是第一个分组，所以(?(1)\d|abc)中的 (1) 分组 1 是存在的
            - 所以会匹配 \d
'''


res = re.match('(\d)abc(?(1)\d|abc)', '1abc2')
print res.group()