'''
    字符串拼接
'''

str1 = 'very'
str2 = 'good'

print str1 + ' ' + str2


'''
    字符串和数字拼接
    字符和数字不能直接用+相加
    * 一种解决方法是，用str()把数字转换成字符串
    * 还有一种方法，就是用%对字符串进行格式化 %d' %num
    * %d会被%后面的值替换

    %d : 格式化整数
    %f ：格式化浮点小数 (%.2f : 保留两位小数)
    %s ：替换字符串 
'''

age = 18
#print 'My age is :' + age   这个输出会报错

print 'My age is: ' + str(age)

print 'My age is: %d' %age # %d 会被 % 后面的值替换

price = 4.99
print 'The price is: %f' %price #结果：Price is 4.990000

print 'The price is: %.2f' %price #保留两位小数 结果：The price is: 4.99


name = 'Shihongji'
print '%s is a liang min' %name


score = 90
print "%s's score is %d" %(name, score) #多个值替换


'''
    小游戏
'''

print '\n--------------小游戏------------\n'

from random import randint

num = randint(0,10)
print num

answer = 0;

print '猜数字游戏,请输入任意整数：'

while answer != num:
    answer = input()
    if answer > num:
        print '%d is too big' %answer
    if answer < num:
        print '%d is too small' %answer

print '%d is the right answer!' %answer
