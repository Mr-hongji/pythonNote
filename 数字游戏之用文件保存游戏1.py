# -*- coding: cp936 -*-
'''
    猜数字游戏

    新添内容：
    
        * 在本地新建guestNumberGame文本文件，写入‘0 0 0’并保存
        * 读取本地游戏数据（游戏总次数、最快猜出来的轮数、猜过的总轮数）
        
'''


print '\n----猜数字游戏----\n'


f = file('guestNumberGame.txt')
data = f.read()
f.close()


l = data.split()

sum_times = int(l[0])

min_times = int(l[1])

total_times = int(l[2])

if sum_times == 0:
    avg_times = 0
else:
    avg_times = total_times / sum_times


print '你已经玩过几次 %d 次, 最少 %d 轮猜出答案, 平均 %.2f 轮才出答案\n' % (sum_times, min_times, avg_times)


from random import randint

def isEqual(num1, num2):
    if num1 < num2:
        print 'too small'
        return False
    if num1 > num2:
        print 'too big'
        return False
    if num1 == num2:
        print 'guest right'
        return True

randomNum = randint(0,100)

print '\n随机生成的数字: ' + str(randomNum) + '\n'

isOk = False

while not isOk:
    answer = input()
    isOk = isEqual(answer, randomNum)

