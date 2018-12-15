'''
语法为：

   while 条件:
       循环执行的语句

    同if一样，注意冒号，注意缩进。
'''

num = 30
answer = 0

print "年龄猜猜猜....."

while answer != num:

    answer = input()
    
    if answer > num:
        print "big 猜错啦!"

    if answer < num:
        print "small 猜错啦!"

print "恭喜，猜对啦！"
