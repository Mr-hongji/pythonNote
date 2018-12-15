# -*- coding: cp936 -*-
'''
    猜数字游戏

    添加内容：
    
        * 存储多组成绩。
        * 玩家需要在游戏开始前，输入自己的名字
        * 游戏会根据这个名字记录每个玩家的成绩

'''


print '\n----猜数字游戏----\n'

input_player_name = raw_input('输入你的名字：')

f = file('guestNumberGame.txt')
player_data = f.readlines()
f.close()

sum_times = 0
min_times = 0
total_times = 0

currentPlyer = []
currentIndex = 0
has_player_name = False  # 注意：定义Boolean变量时 False 和 True 中的 F 和 T 是大写

for player in player_data:

    currentPlyer = player.split()
    
    if str(currentPlyer[0]) == input_player_name:
        
        sum_times = int(currentPlyer[1]) #记录玩过几次游戏

        min_times = int(currentPlyer[2]) #记录每次游戏猜对所用最少轮数

        total_times = int(currentPlyer[3]) #记录总共玩了多少轮

        has_player_name = True
        
        break

    currentIndex += 1


if sum_times == 0:
    avg_times = 0
else:
    avg_times = total_times / sum_times


print '你已经玩过几次 %d 次, 最少 %d 轮猜出答案, 平均 %.2f 轮才出答案\n' % (sum_times, min_times, avg_times)


from random import randint

def isEqual(num1, num2):
    if num1 < num2:
        print '\ntoo small'
        return False
    if num1 > num2:
        print '\ntoo big'
        return False
    if num1 == num2:
        print '\nguest right'
        return True

randomNum = randint(0,100)

print '\n随机生成的数字: ' + str(randomNum) + '\n'

isOk = False


currenttimes = 0; #记录当前游戏猜对所用轮数


while not isOk:
    total_times += 1
    currenttimes += 1
    answer = input('输入所猜数字：')
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

currentPlyer = []

currentPlyer.append(input_player_name)
currentPlyer.append(str(sum_times))
currentPlyer.append(str(min_times))
currentPlyer.append(str(total_times))


current_plyer_info = ' '.join(currentPlyer) + '\n'

if has_player_name:
    
    player_data[currentIndex] = current_plyer_info
    
else:
    
    player_data.append(current_plyer_info)


#print player_data

f = file('guestNumberGame.txt', 'w')
f.writelines(player_data) # 注意：向文件中写 List 时必须要是用 writelines() 函数
f.close()



