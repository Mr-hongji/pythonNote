'''

if elif else


语法为：

   if 条件:
       选择执行的语句

特别说明：条件后面的冒号不能少，同样必须是英文字符。
特别特别说明：if内部的语句需要有一个统一的缩进，一般用4个空格。python用这种方法替代了其他很多编程语言中的{}。
你也可以选择1/2/3...个空格或者按一下tab键，但必须整个文件中都统一起来。
千万不可以tab和空格混用，不然就会出现各种莫名其妙的错误。所以建议都直接用4个空格。
'''

num=30

print "年龄猜猜猜。。。"

print "How old I am?"

answer = input()

if answer > num:
    print "big   猜错啦!"


elif answer < num:
    print "small   猜错啦!"


else :
    print "猜中啦!"





'''

    if嵌套
    
    格式：

        if 条件1:
           if 条件2:
               语句1
           else:
               语句2
        else:
           if 条件2:
               语句3
           else:
               语句4
'''





