# -*- coding: cp936 -*-
'''
    ��������Ϸ

    ������ݣ�
    
        * �洢����ɼ���
        * �����Ҫ����Ϸ��ʼǰ�������Լ�������
        * ��Ϸ�����������ּ�¼ÿ����ҵĳɼ�

'''


print '\n----��������Ϸ----\n'

input_player_name = raw_input('����������֣�')

f = file('guestNumberGame.txt')
player_data = f.readlines()
f.close()

sum_times = 0
min_times = 0
total_times = 0

currentPlyer = []
currentIndex = 0
has_player_name = False  # ע�⣺����Boolean����ʱ False �� True �е� F �� T �Ǵ�д

for player in player_data:

    currentPlyer = player.split()
    
    if str(currentPlyer[0]) == input_player_name:
        
        sum_times = int(currentPlyer[1]) #��¼���������Ϸ

        min_times = int(currentPlyer[2]) #��¼ÿ����Ϸ�¶�������������

        total_times = int(currentPlyer[3]) #��¼�ܹ����˶�����

        has_player_name = True
        
        break

    currentIndex += 1


if sum_times == 0:
    avg_times = 0
else:
    avg_times = total_times / sum_times


print '���Ѿ�������� %d ��, ���� %d �ֲ³���, ƽ�� %.2f �ֲų���\n' % (sum_times, min_times, avg_times)


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

print '\n������ɵ�����: ' + str(randomNum) + '\n'

isOk = False


currenttimes = 0; #��¼��ǰ��Ϸ�¶���������


while not isOk:
    total_times += 1
    currenttimes += 1
    answer = input('�����������֣�')
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
f.writelines(player_data) # ע�⣺���ļ���д List ʱ����Ҫ���� writelines() ����
f.close()



