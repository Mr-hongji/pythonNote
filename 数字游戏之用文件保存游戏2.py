# -*- coding: cp936 -*-
'''
    ��������Ϸ

		������ݣ�
		
        * ��¼����Ϸ�ܴ��������³������������¹��������������ݵ�����

'''


print '\n----��������Ϸ----\n'


f = file('guestNumberGame.txt')
data = f.read()
f.close()


l = data.split()

sum_times = int(l[0]) #��¼���������Ϸ

min_times = int(l[1]) #��¼ÿ����Ϸ�¶�������������

total_times = int(l[2]) #��¼�ܹ����˶�����

if sum_times == 0:
    avg_times = 0
else:
    avg_times = total_times / sum_times


print '���Ѿ�������� %d ��, ���� %d �ֲ³���, ƽ�� %.2f �ֲų���\n' % (sum_times, min_times, avg_times)


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

print '\n������ɵ�����: ' + str(randomNum) + '\n'

isOk = False


currenttimes = 0; #��¼��ǰ��Ϸ�¶���������


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

�Ż��������£�

'''

if min_times == 0 or min_times > currenttimes:
    min_times = currenttimes


sum_times += 1


result = '%d %d %d' % (sum_times, min_times, total_times)

f = file('guestNumberGame.txt', 'w')
f.write(result)
f.close()



