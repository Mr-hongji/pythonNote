# -*- coding: cp936 -*-
'''
    ��������Ϸ

    �������ݣ�
    
        * �ڱ����½�guestNumberGame�ı��ļ���д�롮0 0 0��������
        * ��ȡ������Ϸ���ݣ���Ϸ�ܴ��������³������������¹�����������
        
'''


print '\n----��������Ϸ----\n'


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

while not isOk:
    answer = input()
    isOk = isEqual(answer, randomNum)

