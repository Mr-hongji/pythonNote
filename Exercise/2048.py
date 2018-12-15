# -*- coding:utf-8 -*-

import random
import sys

class Square:
    cloum = 1
    row = 1
    showNum = ' '
    alreadyAdded = False

    def __init__(self, cloum, row):
        self.cloum = cloum
        self.row = row


datas = {} # 全部数据方格

# 初始化数据
def initData():
    datas.clear()
    for rowIndex in range(1, 5):
        for cloumIndex in range(1, 5):
            obj = Square(rowIndex, cloumIndex)
            datas[str(rowIndex) + str(cloumIndex)] = obj

    print '得分：'
    randomNum()
    drawingSquare()



# 产生随机数到空闲方格
def randomNum():
    empty = {}
    # 从空闲方格字典中随机选出一个方格
    for key in datas:
        if datas[key].showNum == ' ':
            empty[key] = datas[key]

    key = random.sample(empty,1)
    key = ''.join(key)

    # 随机生成2或4
    num = ['2','4']
    n = random.sample(num, 1)
    n = ''.join(n)

    print('randomNum = ',key, n)
    # 更新数据
    datas[key].showNum = n
    # delEmptyDictData(key)

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
            pane = datas[str(rIndex) + str(cIndex)]
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

# 降序排列
def comp(x, y):
    if x < y:
        return 1
    elif x > y:
        return -1
    else:
        return 0


# 根据direction（方向）计算新的数据
def calculateNewData(direction):
    cl = range(1, 5)
    cl.sort(comp)

    if direction == 'w':
        calculateUpMoveData(range(1, 5), range(1, 5), 'w')
        print '上'

    elif direction == 's':
        calculateDownMoveData(range(1, 5), cl, 's')
        print '下'

    elif direction == 'a':
        # 向左移动时 rowIndex从 1 到 5， cloumIndex是从 5 到 1
        calculateLeftMoveData(range(1, 5), range(1, 5), 'a')
        print '左'

    elif direction == 'd':
        # 向右移动时 rowIndex从 1 到 5， cloumIndex是从1 到 5
        calculateRightMoveData(range(1 ,5), cl, 'd')
        print '右'

    else:
        print '命令输入错误，重新输入'
        return False

    randomNum()
    drawingSquare()

# 计算向右移动数据
def calculateRightMoveData(rowList, columList, direction):
    print columList
    for rIndex in rowList:
        for cIndex in columList:

            ri = str(rIndex)
            ci = str(cIndex)

            # 向左（右）移动时，改变列索引，行索引不变
            currentPane = datas[ri + ci]

            if currentPane.showNum != ' ':
                cloumSum = len(columList) # 总列数

                # 改变行索引
                nextCIndex = getNextIndex(cIndex, direction)
                while(nextCIndex <= cloumSum):
                    nextPane = datas[ri + str(nextCIndex)]
                    if nextPane.showNum == ' ': # 如果下一个值是空则继续向下循环
                        nextPane.showNum = currentPane.showNum
                        currentPane.showNum = ' '
                        currentPane = nextPane
                        nextCIndex = getNextIndex(nextCIndex, direction)
                    elif nextPane.showNum == currentPane.showNum and not nextPane.alreadyAdded:
                        # 前面方格中的数据等于当前方格中的数据，并且前面方格中的数据不是通过相加之后的结果
                        # 比如 4、2、2、' '  向右移动后正确结果应该是：' '、' '、4、4
                        # 如果不对alreadyAdded做判断得到的结果是：' '、 ' '、 ' '、 8，导致最后4和也想加了
                        nextPane.showNum = str(int(currentPane.showNum) + int(nextPane.showNum))
                        nextPane.alreadyAdded = True
                        currentPane.showNum = ' '
                        nextCIndex = cloumSum + 1  # 设置nextCIndex来结束循环
                    else:
                        nextCIndex = cloumSum + 1  # 设置nextCIndex来结束循环

# 计算向左移动数据
def calculateLeftMoveData(rowList, columList, direction):
    print columList
    for rIndex in rowList:
        for cIndex in columList:

            ri = str(rIndex)
            ci = str(cIndex)

            # 向左（右）移动时，改变列索引，行索引不变
            currentPane = datas[ri + ci]

            if currentPane.showNum != ' ':

                # 改变行索引
                nextCIndex = getNextIndex(cIndex, direction)
                while(nextCIndex >= 1):
                    nextPane = datas[ri + str(nextCIndex)]
                    if nextPane.showNum == ' ': # 如果下一个值是空则继续向下循环
                        nextPane.showNum = currentPane.showNum
                        currentPane.showNum = ' '
                        currentPane = nextPane
                        nextCIndex = getNextIndex(nextCIndex, direction)
                    elif nextPane.showNum == currentPane.showNum and not nextPane.alreadyAdded:
                        nextPane.showNum = str(int(currentPane.showNum) + int(nextPane.showNum))
                        nextPane.alreadyAdded = True
                        currentPane.showNum = ' '
                        nextCIndex = 0  # 设置nextCIndex来结束循环
                    else:
                        nextCIndex = 0  # 设置nextCIndex来结束循环


# 计算向下移动数据
def calculateDownMoveData(rowList, columList, direction):
    print columList
    for rIndex in rowList:
        for cIndex in columList:

            ri = str(rIndex)
            ci = str(cIndex)

            # 向上（下）移动时，改变行索引，列索引不变
            currentPane = datas[ci + ri]

            if currentPane.showNum != ' ':
                rowSum = len(rowList)# 总行数

                # 改变行索引
                nextCIndex = getNextIndex(cIndex, direction)
                while(nextCIndex <= rowSum):
                    nextPane = datas[str(nextCIndex) + ri]
                    if nextPane.showNum == ' ': # 如果下一个值是空则继续向下循环
                        nextPane.showNum = currentPane.showNum
                        currentPane.showNum = ' '
                        currentPane = nextPane
                        nextCIndex = getNextIndex(nextCIndex, direction)
                    elif nextPane.showNum == currentPane.showNum and not nextPane.alreadyAdded:
                        nextPane.showNum = str(int(currentPane.showNum) + int(nextPane.showNum))
                        nextPane.alreadyAdded = True
                        currentPane.showNum = ' '
                        nextCIndex = rowSum + 1  # 设置nextRIndex来结束循环
                    else:
                        nextCIndex = rowSum + 1  # 设置nextRIndex来结束循环


# 计算向上移动数据
def calculateUpMoveData(rowList, columList, direction):
    print columList
    for rIndex in rowList:
        for cIndex in columList:

            ri = str(rIndex)
            ci = str(cIndex)

            # 向上（下）移动时，改变行索引，列索引不变
            currentPane = datas[ci + ri]

            if currentPane.showNum != ' ':

                # 改变行索引
                nextCIndex = getNextIndex(cIndex, direction)
                while(nextCIndex >= 1):
                    nextPane = datas[str(nextCIndex) + ri]
                    if nextPane.showNum == ' ': # 如果下一个值是空则继续向下循环
                        nextPane.showNum = currentPane.showNum
                        currentPane.showNum = ' '
                        currentPane = nextPane
                        nextCIndex = getNextIndex(nextCIndex, direction)
                    elif nextPane.showNum == currentPane.showNum and not nextPane.alreadyAdded:
                        nextPane.showNum = str(int(currentPane.showNum) + int(nextPane.showNum))
                        nextPane.alreadyAdded = True
                        currentPane.showNum = ' '
                        nextCIndex = 0  # 设置nextRIndex来结束循环
                    else:
                        nextCIndex = 0  # 设置nextRIndex来结束循环


def getNextIndex(index, direction):
    if direction == 'w' or direction == 'a':
        index -= 1

    elif direction == 's' or direction == 'd':
        index += 1

    return index

def checkoutEle(key):
    return key in datas

# 开始
def start():
    initData()
    b = True

    while (b):
       operation =  raw_input('input Operation (W)上 (S)下 (A)左 (D)右 (R)重来 (Q)退出：')

       operation = str(operation)
       if operation == 'q':
           print '退出程序'
           sys.exit(0)

       elif operation == 'r':
           print '重来'
           start()

       else:
           calculateNewData(operation)


start()