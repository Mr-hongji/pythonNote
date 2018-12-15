# -*- coding: cp936 -*-
'''
    猜数字游戏

		添加内容：
		
        * 记录（游戏总次数、最快猜出来的轮数、猜过的总轮数）数据到本地

'''


print '\n----猜数字游戏----\n'


f = file('guestNumberGame.txt')
data = f.read()
f.close()


l = data.split()

sum_times = int(l[0]) #记录玩过几次游戏

min_times = int(l[1]) #记录每次游戏猜对所用最少轮数

total_times = int(l[2]) #记录总共玩了多少轮

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


currenttimes = 0; #记录当前游戏猜对所用轮数


while not isOk:
    total_times += 1
    currenttimes += 1
    answer = input()
    isOk = isEqual(answer, randomNum)


'''
if min_times == 0:
    min_times = currenttimes

elif min_times > currenttimes:
    min_times = currenttimes

优化更新如下：

'''

if min_times == 0 or min_times > currenttimes:
    min_times = currenttimes


sum_times += 1


result = '%d %d %d' % (sum_times, min_times, total_times)

f = file('guestNumberGame.txt', 'w')
f.write(result)
f.close()



