'''
    数据类型
    
        * 字符串
        * 整数
        * 小数（浮点数）
        * bool类型

    转换
        int(x) #把x转换成整数
        float(x) #把x转换成浮点数
        str(x) #把x转换成字符串
        bool(x) #把x转换成bool值

    并不是所有的值都能做类型转换，比如int('abc')同样会报错，python没办法把它转成一个整数。
'''

#print 'Price: ' + 4 #这个写法是错误的,数字不能和字符串相加

#print 'Price: %d' %'123' #这个写法是错误的,%d需要的是一个整数，而'123'是字符串

print 'Price: ' + str(4)

print 'Price: %d' %int('123')


