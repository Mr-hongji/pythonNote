'''
    python中，以下数值会被认为是False：
    
        * 为0的数字，包括0，0.0
        * 空字符串，包括''，""
        * 表示空值的None
        * 空集合，包括()，[]，{}
        * 其他的值都认为是True。
'''
print bool(-123)
print bool(0)
print bool('abc')
print bool('False')
print bool('')
print bool(' ') #结果是True，一个空格也不能算作空字符串
