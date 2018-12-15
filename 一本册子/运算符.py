num=30
print "年龄猜猜猜。。。"

print "How old I am?"

answer = input()

result = answer > num
print "big   请继续猜！"
print answer


result = answer < num
print "small   请继续猜！"
print answer


result = answer == num
print "猜中啦!"
print answer

a = 1 > 2 and 2 > 3
b = 1 > 2
c = not 1 > 2
d = 1 > 2 or 3 > 1

print a
print b
print c
print d
