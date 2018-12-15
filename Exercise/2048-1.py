# -*- coding:utf-8 -*-

''''''

'''

实现思路（以向右滑动为例）：

rowIndex + cloumIndex:

方格坐标：       11             12          13             14
            +------------+------------+------------+------------+
            |     2      |     8      |            |     8     |
            +------------+------------+------------+------------+

从右边开始，当前方格同相邻右边方格比较，遇到右边方格数据是空，则 右边方格数据 = 当前方格数据，
交换当前方格和右侧方格 ：当前方格 = 右边方格
继续向右比较，
直到遇到一个非空方格，然后比较当前方格数据和右侧方格数据的大小，如果不相等，则跳出循环，如果相等，
则 右侧方格数据 = 当前方格数据 + 右侧方格个数据，清除当前方格数据，跳出循环

比如把第三列  12 向右移动

    第一次移动： 12 右边的 13 值是空，把12得值右移到13中， 清空12中的值 ，然后13变成当前方格

    输出结果：2 '' 8 8

    第二移动：13 同右侧方格14进行比较

        如果13值等于14值，则 14中的值 = 13值 + 14值， 清空13中的值 ，结束对比循环   输出结果： 2 '' '' 16

        如果13值不等于14值，则不做任何处理，结束对比循环


'''

import random
import sys

squares = {} # 全部数据方格
sumScore = 0 # 最高得分
score = 0   # 本次得分
playerName = '' # 玩家名称
scoreFileName = '2048Score.txt'
historyMaxScore = 0

# 方格
class Square:
    cloum = 1
    row = 1
    showNum = ' '
    alreadyAdded = False

    def __init__(self, row, cloum):
        self.cloum = cloum
        self.row = row


# 初始化数据
def initData():
    squares.clear()
    for rowIndex in range(1, 5):
        for cloumIndex in range(1, 5):
            obj = Square(rowIndex, cloumIndex)
            squares[str(rowIndex) + str(cloumIndex)] = obj

    randomNum()
    showScore()
    drawingSquare()


# 产生随机数到空闲方格
def randomNum():
    empty = {}
    # 从空闲方格字典中随机选出一个方格
    for key in squares:
        if squares[key].showNum == ' ':
            empty[key] = squares[key]

    key = random.sample(empty,1)
    key = ''.join(key)

    # 随机生成2或4
    num = ['2','4']
    n = random.sample(num, 1)
    n = ''.join(n)

    square = empty[key]

    # print('randomNum = ', n, ' 方格位置：', key)

    # 更新数据
    squares[key].showNum = n
    # delEmptyDictData(key)

    return len(empty)

# 读文件
def readFile():
    f = open(scoreFileName, 'r')
    lines = f.readlines()
    f.close()
    return lines

# 写文件
def writeFile(lines):
    f = open(scoreFileName, 'w')
    print ''.join(lines)
    f.writelines(''.join(lines))
    f.close()

def recordTheScore():

    if sumScore > int(historyMaxScore):

        print ('记录得分')

        lines = readFile()

        scoreInfo = playerName + ' ' + str(sumScore) + '\n'
        for index, d in enumerate(lines):
            l = d.split(' ')
            if l[0] == playerName:
                lines[index] = scoreInfo
                break
        else:
            lines.append(scoreInfo)

        if len(lines) == 0:
            lines.append(scoreInfo)

        writeFile(lines)



# 结束程序
def terminationRoutine():
    print 'Game Over!'
    recordTheScore()
    sys.exit(0)

'''
    当只剩最后一个空白方格时，开始比对每行每列中每个方格前面的数据，
    是否有数据为空或者数据相同的方格，如果没有：
        1、则结束循环，判断游戏结束
    
    ri 行索引
    ci 列索引
    ranNum 新生成的随机数
'''
def checkGameOver():
    rowList = range(1, 5)
    columList = range(1, 5)
    gameOver = True

    while(True):
        for direction in ('a', 'w', 0): # 使用向左移动来对比行数据，用向上移动来对比列数据
            if not direction:
                break
            for rIndex in rowList:
                for cIndex in columList:
                    ri = str(rIndex)
                    ci = str(cIndex)

                    currentPane = squares[ci + ri] if direction == 'w' else squares[ri + ci]

                    if currentPane.showNum == ' ':
                        gameOver = False  # 总行数
                        break

                    nextCIndex = getNextIndex(cIndex, direction)

                    if(nextCIndex < 1):
                        continue

                    nextPane = squares[str(nextCIndex) + ri] if direction == 'w' else squares[ri + str(nextCIndex)]
                    if nextPane.showNum == ' ' or nextPane.showNum == currentPane.showNum:
                        gameOver = False
                        cIndex = -1
                        break
                    else:
                        continue

                if not gameOver:
                    break

        if not direction:
            break

        if not gameOver:
            break

    # print('gameOver = ', gameOver)
    if gameOver:
        terminationRoutine()


# 绘制方格
#args 一行中每个方格的
def drawingSquare():

    paneWidth = 12 # 方格宽度12个-
    line = '|'
    hline1 = '+' + '-' * 12
    hline = hline1 * 4 + '+'

    print hline  # 绘制方格横线

    for rIndex in range(1, 5):
        s = ''
        for cIndex in range(1, 5):
            pane = squares[str(rIndex) + str(cIndex)]
            showNum = pane.showNum
            pane.alreadyAdded = False # 还原标识符

            # 计算数据在方格内的两边间隔，保证数据过长方格不乱
            bothSides = (paneWidth - (len(showNum))) / 2
            bothSides = int(bothSides)
            vline1 = line + ' ' * bothSides
            vline2 = ' ' * (len('-' * paneWidth) - len(vline1 + showNum))
            s += vline1 + showNum + vline2 + ' '

        print s + line
        print hline

# 根据direction（方向）计算新的数据
def calculateNewData(direction):
    cl = range(1, 5)
    cl.sort(reverse=True) # 降序排序

    if direction == 'w':
        createRandomNum = calculateUpDownMoveData(range(1, 5), range(1, 5), 'w')

    elif direction == 's':
        createRandomNum = calculateUpDownMoveData(range(1, 5), cl, 's')

    elif direction == 'a':
        # 向左移动时 rowIndex从 1 到 4， cloumIndex是从 4 到 1
        createRandomNum = calculateLeftRightMoveData(range(1, 5), range(1, 5), 'a')

    elif direction == 'd':
        # 向右移动时 rowIndex从 1 到 4， cloumIndex是从 4 到 1
        createRandomNum = calculateLeftRightMoveData(range(1 ,5), cl, 'd')

    else:
        print '命令输入错误，重新输入'
        return False

    emptyLen = None
    if createRandomNum:
        emptyLen = randomNum()

    showScore()
    drawingSquare()

    # 给最后一个空白方格生成数据后， 检查每行和每列中相邻的方格中是否存在空数据或相同的数据
    if emptyLen == 1:
        checkGameOver()


# 计算左右移动数据
def calculateLeftRightMoveData(rowList, columList, direction):
    global score
    score = 0

    # 是否生成新的随机数字, 数字没有移动或改变时，不生成新的随机数
    createRandomNum = False

    for rIndex in rowList:
        for cIndex in columList:

            ri = str(rIndex)
            ci = str(cIndex)

            # 向左（右）移动时，改变列索引，行索引不变
            currentPane = squares[ri + ci]

            if currentPane.showNum != ' ':
                cloumSum = len(columList) # 总列数

                # 改变行索引
                nextCIndex = getNextIndex(cIndex, direction)
                while(nextCIndex >= 1 if direction == 'a' else nextCIndex <= cloumSum):
                    nextPane = squares[ri + str(nextCIndex)]
                    if nextPane.showNum == ' ': # 如果下一个值是空则继续向下循环
                        nextPane.showNum = currentPane.showNum
                        currentPane.showNum = ' '
                        currentPane = nextPane
                        nextCIndex = getNextIndex(nextCIndex, direction)
                        createRandomNum = True
                    elif nextPane.showNum == currentPane.showNum and not nextPane.alreadyAdded:
                        # 前面方格中的数据等于当前方格中的数据，并且前面方格中的数据不是通过相加之后的结果
                        # 比如 4、2、2、' '  向右移动后正确结果应该是：' '、' '、4、4
                        # 如果不对alreadyAdded做判断得到的结果是：' '、 ' '、 ' '、 8，导致最后4和也相加了
                        nextPane.showNum = str(int(currentPane.showNum) + int(nextPane.showNum))
                        nextPane.alreadyAdded = True
                        currentPane.showNum = ' '
                        createRandomNum = True
                        # 在函数内使用全局变量赋值，那该变量会自动转变为局部变量
                        # 解决办法：使用 global score
                        global sumScore
                        sumScore += int(nextPane.showNum)
                        score += int(nextPane.showNum)
                        nextCIndex = 0 if direction == 'a' else cloumSum + 1  # 设置nextCIndex来结束循环
                    else:
                        nextCIndex = 0 if direction == 'a' else cloumSum + 1  # 设置nextCIndex来结束循环

    return createRandomNum

# 计算上下移动数据
def calculateUpDownMoveData(rowList, columList, direction):
    global score
    score = 0

    createRandomNum = False

    for rIndex in rowList:
        for cIndex in columList:

            ri = str(rIndex)
            ci = str(cIndex)

            # 向上（下）移动时，改变行索引，列索引不变
            currentPane = squares[ci + ri]

            if currentPane.showNum != ' ':
                rowSum = len(rowList)# 总行数

                # 改变行索引
                nextCIndex = getNextIndex(cIndex, direction)
                while(nextCIndex >= 1 if direction == 'w' else nextCIndex <= rowSum):
                    nextPane = squares[str(nextCIndex) + ri]
                    if nextPane.showNum == ' ': # 如果下一个值是空则继续向下循环
                        nextPane.showNum = currentPane.showNum
                        currentPane.showNum = ' '
                        currentPane = nextPane
                        createRandomNum = True
                        nextCIndex = getNextIndex(nextCIndex, direction)
                    elif nextPane.showNum == currentPane.showNum and not nextPane.alreadyAdded:
                        nextPane.showNum = str(int(currentPane.showNum) + int(nextPane.showNum))
                        nextPane.alreadyAdded = True
                        currentPane.showNum = ' '
                        createRandomNum = True
                        # 在函数内使用全局变量赋值，那该变量会自动转变为局部变量
                        # 解决办法：使用 global score
                        global sumScore
                        sumScore += int(nextPane.showNum)
                        score += int(nextPane.showNum)
                        nextCIndex = 0 if direction == 'w' else rowSum + 1  # 设置nextRIndex来结束循环
                    else:
                        nextCIndex = 0 if direction == 'w' else rowSum + 1  # 设置nextRIndex来结束循环

    return createRandomNum

def getNextIndex(index, direction):
    if direction == 'w' or direction == 'a':
        index -= 1

    elif direction == 's' or direction == 'd':
        index += 1

    return index


def showScore():
    print
    print '昵称：%s   总得分：%i  本次得分：%i  最高得分：%i' % (playerName, sumScore, score, historyMaxScore)


# 获取历史得分
def readHistoricalScore():
    lines = readFile()
    if len(lines) > 0:
        for data in lines:
            l = data.split(' ')
            if l[0] == playerName:
                global historyMaxScore
                historyMaxScore = int(l[1])
                break


#  输入玩家名称
def inputPlayerName():
    while (True):
        global playerName
        playerName = raw_input('Please Input Your Name:')
        if len(playerName.strip()) > 0:
            break


# 开始
def start():

    inputPlayerName()
    readHistoricalScore()

    initData()
    b = True

    while (b):
       operation =  raw_input('input Operation (W)上 (S)下 (A)左 (D)右 (R)重来 (Q)退出：')

       operation = str(operation)
       if operation == 'q':
           terminationRoutine()

       elif operation == 'r':
           print '重来'
           start()

       else:
           calculateNewData(operation)


start()