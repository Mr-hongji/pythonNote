'''

    break
    
        * 彻底地跳出循环


    continue

        * 只是跳过本次循环，直接进入下一次循环


    注意：
        * 无论是continue还是break，其改变的仅仅是当前所处的最内层循环的运行
        * 如果外层还有循环，并不会因此略过或跳出
'''


print '\n break 示例：\n'

for i in range(10):
    a = input()
    if a == 'EOF':
        break
print '循环结束....'



print '\n continue 示例: \n'

for n in range(10):
    if n == 5: #只会跳过 n==5 的这一次循环  会继续执行 n==6、7、8、9的循环
        continue
    print n
print '循环结束....'





'''

    break, continue 小示例：

'''


i = 0
while i < 5:
    i += 1
    for j in range(3):
        print j
        if j == 2:
            break
    for k in range(3):
        if k == 2:
            continue
        print k
    if i >3:
        break
    print i




