# -*- coding:utf-8 -*-
''''''

'''

周几 月 日   时间    年           邮箱

Thu Jul 22 19:21:19 2004::izsp@dicqdhytvhv.edu::1090549279-4-11
Sun Jul 13 22:42:11 2008::zqeu@dxaibjgkniy.com::1216014131-4-11
Sat May 5 16:36:23 1990::fclihw@alwdbzpsdg.edu::641950583-6-10
Thu Feb 15 17:46:04 2007::uzifzf@dpyivihw.gov::1171590364-6-8
Thu Jun 26 19:08:59 2036::ugxfugt@jkhuqhs.net::2098145339-7-7
Tue Apr 10 01:04:45 2012::zkwaq@rpxwmtikse.com::1334045085-5-10


'''

import  re

def test(restr, * args):
    for s in args:
        res = re.match(restr, s)
        print res.group()

'''

练习1-1:
 
    识别后续的字符串：“bat”、“ bit”、“ but”、“ hat”、“ hit”或者“hut”。

'''

test('[bh][aiu]t', 'bat','bit', 'but', 'hat', 'hit', 'hut')


'''

练习1-2:

    匹配由单个空格分隔的任意单词对，也就是姓和名。

'''

test('\w+\s\w+', 'shi hongji')



'''

练习1-3:

    匹配由单个逗号和单个空白符分隔的任何单词和单个字母，如姓氏的首字母。

'''

test(r'\w+\s\w+,\s\w+', 'adfaf aa, dadada')


'''

练习1-4:

    匹配所有有效 Python 标识符的集合。
    
    有效 Python 标识符:在python里, 标识符有字母、数字、下划线组成。
    所有标识符可以包括英文、数字以及下划线(_),但不能以数字开头

'''

test('[\w+_+]\w+', 'a_123A','_a123A')


'''

练习1-5:

    根据读者当地的格式，匹配街道地址（使你的正则表达式足够通用，来匹配任意数
量的街道单词，包括类型名称）。

    例如，美国街道地址使用如下格式： 1180 Bordeaux Drive。使你的正则表达式足够灵活，以支持多单词的街道名称，
    如 3120 De la Cruz Boulevard。

'''

test('\d+[\w\s]+', '1180 Bordeaux Drive','3120 De la Cruz Boulevard')
test('\d+.+', '1180 Bordeaux Drive','3120 De la Cruz Boulevard')


'''

练习1-6:

    匹配以 “www”起始且以 “.com”结尾的简单 Web 域名；
    例如， www://www.yahoo.com/。
    
    选做题： 你的正则表达式也可以支持其他高级域名，
    如.edu、 .net 等（例如，http://www.foothill.edu）。

'''

test('\w+://www.\w+.com/', 'www://www.yahoo.com/')

test('\w+://www.\w+.(com|net|edu|org)', 'http://www.foothill.edu',
     'http://www.foothill.org', 'http://www.foothill.com',
     'http://www.foothill.net')

'''

练习1-7:

   匹配所有能够表示 Python 整数的字符串集。

'''

test(r'-?\d+', '-123141234', '123141234')