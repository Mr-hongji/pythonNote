#encoding=GBK
 #------------------------------------- ��һ�� ------------------------------------#


print
print '��һ��'

'''

    * ���� / ����, ��������С�����ֱ��س���ֻ�����������֣������������룩 �磺  1 / 2

    * ʵ����Python�г�Ϊ��������Float��
    * �������������������һ����Ϊ�����������ҲΪ������ �磺 1.0 / 2, 1 / 2.0,  1.0 / 2.0

    * ͨ�������ֻ��Ҫ��ͨ�㷨���� 1 / 2 = 0.5 ,�������£�
        * �ڳ���ǰ���� from __future__ import division (__future__ ǰ���������»���)
        * ��ֱ���ڽ�������ִ����

    * ������ ��2 ** 3�� 
  
'''

print  1 / 2 #��� 0

print 1.0 / 2 #��� 0.5
print 1 / 2.0 #��� 0.5
print 1.0 / 2.0 #��� 0.5

print 2 ** 3 #��� 8



'''

    ת���ַ��������ֻ���

        * str������������ֵת��Ϊ������ַ�����ʽ ----- ���ô˷�ʽ
        * repr��������������һ���ַ���

'''

temp = 10

print 'The temperature is: ' + str(temp)
print 'The temperature is: ' + repr(temp)



'''

    ԭʼ�ַ������ r
    
'''

print 'Hello\nWorld' # ����ỻ�� ��Ϊ\n�ǻ��з�
print 'Hello''World'
print 'Hello','World'
print 'Hello World'

print 'C:\nowhere' 

# ��ʱ�����������ӡ·����Ҫʹ�� r ԭʼ�ַ���ʶ

print r'C:\nowhere'
print r'C:\nowhere\\'
print r'C:\nowhere' '\\'

print r'Let\'s go!' # ��� Let\'s go!

#��

print 'C:\\nowhere' # �˷�ʽ���ʺϳ��ַ��� �磺 C:\\nwhere\\bozz\\frozz  ��Ҫд�ܶ෴б��






 #------------------------------------- �ڶ��� ------------------------------------#

print
print '�ڶ���'



'''
    �б���

        * ����������������������������0
        * �����Ǹ���ʱ����ʼ������������ڽ��������� numbers[8:3:-2] 8(��ʼ����) > 3��������������
        * �����Ǹ���ʱ���������β��������ȡԪ�أ�ֱ����һ��Ԫ��
        * ����������ʱ��������е�ͷ����ʼ������ȡԪ��
'''

numbers = [1,2,3,4,5,6,7,8,9,10]

print numbers[:5:1] # [1,2,3,4,5] ��������Ϊ1 ��Ĭ�Ͼ���1��

print numbers[:5:2] # [1,3,5]

print numbers[8:3:-2] # [9,7,5]




'''

    �������

        * ������ͬ���͵����в��ܽ������Ӳ���

'''

print [1,2,3] + [4,5,6]



'''

    �˷�

        ����һ��������ĵط�
'''

print 'Python' * 5 # ��ͬ�� 'Python' + 'Python' + 'Python' + 'Python' + 'Python'

print [10] * 5 # ������������� ��ͬ�� [10] + [10] + [10] + [10] + [10] 




'''

    in �����

        * ���һ��ֵ�Ƿ���������
        * ���ڷ���True  �����ڷ���False
    
'''

name = '�̺��'

print '��' in name
print '�鼪' in name

names = ['�̺��', '�̲���ɵ', '�̺鼪']

print '�̺��' in names

print '�鼪' in names


database = [
    ['honghong', '123'],
    ['hongji', '1234'],
    ['shihongji', '000000']
]

name = raw_input('�����û���:')
pin = raw_input('PIN��:')
if [name,pin] in database:
    print 'User Acc granted'


'''

    len() �����б���
       
    min() �����б�����СԪ��
    
    max() �����б������Ԫ��

    max��min����������һ�����У����Զ������ֱ����Ϊ����

    list() ���ַ���ǿת���ַ�����

'''
#l = [10,4,7,2,3,0]
l = ['shihongji', 'shihonghong', 'shixiaohong']
print len(l)
print min(l)
print max(l)

print min(1,5,2,1)
print max(1,5,2,3)

print list('shi') #���['s','h','i'] 




'''

    ��Ƭ��ֵ
    
'''

name = list('shihongji')

name[7:] = list('hong') # ['s', 'h', 'i', 'h', 'o', 'n', 'g', 'h', 'o', 'n', 'g']
print name

numbers = [1,2,4,5]
numbers[1:3] = [3]
print numbers

numbers = [3,1,4,5,8,10]
print numbers[:3:2] #���[3,4]
numbers[:3:2] = [9] * 2 #ʵ�ʾ��ǰ�[3,4] �滻��ֵ [9] * 2 �����Ǽ��ͳ˼�
print numbers



'''

    extend() ���б�ĩβһ����׷����һ�������еĶ��ֵ

    a.extend(b) extend�����޸��˱���չ���У������е�a��

    a + b ������һ���µ��б�(�����е�c)
'''

a = [1,2,3]
b = [4,5,6]

a.extend(b) # ��b�б�Ԫ��׷�ӵ�a�б��

print a

a = [9,8,7]
b = [4,5,6]

c = a + b
print a
print b
print c


'''

    index(Ԫ��ֵ) ����Ԫ�����б��е�����

    insert��Ҫ���������λ��, Ԫ��ֵ�����б��в���Ԫ��

    pop() �Ƴ��б�Ԫ�أ�Ĭ���Ƴ����һ�����������ظ�Ԫ�ص�ֵ
    pop(0) �Ƴ��б��0��Ԫ��

    remove() �Ƴ��б��е�ĳ��ֵ

    reverse() ���б��е����ݷ����� [1,2,3] reverse() �� ���[3,2,1]

    list.sort() �� sorted(list) ����(Ĭ����������)��

        * sort() ��ԭ�б����򣬻�ı�ԭ�б�
        * sorted() �����������µ��б�ԭ�б���
'''

l = [1,2,3,'shi', 'hong', 'ji']

index = l.index('shi')
print index # 3

l.insert(0, 'honghong')
print l # ['honghong', 1, 2, 3, 'shi', 'hong', 'ji']

l.pop()
print l # ['honghong', 1, 2, 3, 'shi', 'hong']

l.pop(0)
print l # [1, 2, 3, 'shi', 'hong']

l.remove('hong')
print l # [1, 2, 3, 'shi']

l.reverse()
print l # ['shi', 3, 2, 1]

l = [2,3,5,'shi', 'hong', 'ji']
l.sort()
print l # [2, 3, 5, 'hong', 'ji', 'shi']

l = [2,3,5,'shi', 'hong', 'ji']
ll = sorted(l)
print l # [2, 3, 5, 'shi', 'hong', 'ji']
print ll # [2, 3, 5, 'hong', 'ji', 'shi']



'''

    �б����

        * l[:] = []
        * del l[:]
'''

l = ['1', '2', 3, 4]
print l
l[:] = []
print l

l = ['2', 's', 'f']
print l
del l[:]
print l

'''

    Ԫ��

        �﷨��
            1,2,3 �� ��1,2,3��Ҫ�ö��ŷָ�
                - �ö��ŷָ�ֵ�������Զ�������Ԫ��

        * ���б�һ��Ҳ��һ������
        * Ԫ�鲻���޸ģ�û�����б�һ���ķ���

        Ԫ��Ԫ�ط���ͬ�б����һ�£�

            yz = (1,2,3)
            yz[0]
            yu[:2]

'''

print 1,2,3 # 1,2,3

print (1,2,3) # (1,2,3)

print () # ��Ԫ��

print (42,) # (�� 42,) ����ֻ��һ��Ԫ��ֵ��Ԫ��, ����Ӷ��ţ���ʱֻ��һ��ֵ

print (40 + 2) * 3 # 126

print (40 + 2,) * 3 # (42,42,42) �Ƕ��Ÿı��˽��




'''

    tuple() ����תԪ�飬���ܸ�list()һ������������ǿת

'''

print tuple([1,2,3])
print tuple('abc')







#------------------------------------- ������ ------------------------------------#





'''

    �ַ�����ʽ��

        * %d��%s��%f

   
'''

format = 'doc.%s.%s.cn'
values = ['hongji', 'org']
print format % (values,values)


'''

 ģ���ַ���

        * ��stringģ���ṩ������һ�ָ�ʽ��ֵ�ķ���

'''
from string import Template

s = Template('$x, shihongji $y!')
s = s.substitute(x = 'Hi', y = 'baobao')
print s # Hi, shihongji baobao!


# �滻���ʵ�һ����
s = Template('I\'m shihong${x}')
s = s.substitute(x = 'ji')
print s # I'm shihongji


#ʹ���ֵ�����滻
s = Template('$x is a $y')
d = {}
d['x'] = 'shihonghong'
d['y'] = 'liangmin'
s = s.substitute(d)
print s # shihonghong is a liangmin



#�˴�ע�⣺ %s���ַ�����ʽ�� 1,1,2����������int�������ڴ���ʱ��ת��string
s = '%s plus %s equals %s' % (1,1,2) 
print s # 1 plus 1 equals 2



'''

    �ֶο�Ⱥ;���

        * �����ת�����ֵ����������С�ַ�����
        * �����ǽ����Ӧ�ñ�����С��λ�������ַ�����˵����ת�����ֵ���ܰ���������ַ�������
        * ���������������������õ�ŷָ�
        * ���ֻ�������ȣ��ͱ���������

    ����ʹ��*��Ϊ�ֶο�Ȼ��߾��ȣ��������߶�����*������ʱ�ԶϿ�Ȼ򾫶ȵ���ֵ���Ԫ������ж�ȡ
        
'''

from math import pi

print '%10f' % pi # 10���ַ���� �����'    3.141593' ǰ���ÿո��� 
print '%10.2f' % pi # 10���ַ���� ������2 ���'       3.14' ǰ���ÿո���
print '%.2f' % pi # ������2 ����� '3.14' ������λС��

# ���ַ�����˵����ת�����ֵ���ܰ���������ַ�����
print '%.5s' % 'shihongji is a liangmin' # ��� 'shiho'


print '%.*s' % (5,'shihongji is a liangmin') # ��Ԫ����ȡ��������5 ���shiho

print '%010.2f' % pi #��� 0000003.14  �ַ������0���  010.2f(0:��0��䣬10���ֶο�2:����)

print '%-10.2f' % pi # ���'3.14      '  -10.2f('-':�������)
print '%+10.2f' % pi # ���'      +3.14'  +10.2f('+':���Ҷ���)


'''

    �ַ�����ʽ����ϰ

'''


width = 50 #list width

price_width = 10
item_width = width - price_width

head_format = '%-*s%*s'
format_data = '%-*s%*.2f'

print '=' * width

print head_format % (item_width, 'Item', price_width, 'Price')

print '-' * width

print format_data % (item_width, 'Apple', price_width, 1.586)
print format_data % (item_width, 'Pears', price_width, 1.92)
print format_data % (item_width, 'Cantaloupes', price_width, 2.2521)
print format_data % (item_width, 'Prunes', price_width, 1.98)


'''

ʹ������ʱ����ʽ�����  ԭ��δ֪

print format_data % (item_width, 'ƻ��', price_width, 1.58)
print format_data % (item_width, '��', price_width, 1.92)
print format_data % (item_width, 'ƻ��', price_width, 2.25)
print format_data % (item_width, '�������', price_width, 1.98)

'''


print '=' * width



'''

    �ַ�������

        find(Ҫ���ҵ��ַ�������ʼ�㣬������) �����ַ��������������Ҳ�������-1
        lower() �ַ���תСд
        replace(���滻�ַ��������ַ���)
        strip() ����ַ������˿ո�,Ҳ����ָ��Ҫȥ�����ַ���
        split() �ַ����ָ�
        join() �ַ���ƴ��
'''

name = '$$$ Shihongji Is a Liangmin! $$$'
print name.find('$$$') # 0
print name.find('$$$',1) # 29  ������1��ʼ������
print name.find('a',1,10) # -1 ������1��10֮���Ҳ���a

name1 = name.lower() # ����ı�ԭname��ֵ������������һ���µĸ���
print name1
print name

name1 = name.replace('Shihongji','Shihonghong')# ����ı�ԭname��ֵ������������һ���µĸ���
print name1
print name

name = '   Shihongji Is a Liangmin!   '
print name
name1 = name.strip()# ����ı�ԭname��ֵ������������һ���µĸ���
print name1

name = '*$$$ honghong Is a Liangmin! $$$*'
name1 = name.strip('*$') # ָ��Ҫȥ�����ַ��� *$
print name1



#------------------------------------- ������ ------------------------------------#



'''

    �����ֵ�

        * ֱ��ʹ��{} �磺 d = {}
        * ʹ��dict()����
        
'''

#ֱ��ʹ��{}
d = {} #����һ�����ֵ�
d = {'name':'shihonghong', 'age':30}
print d , d['age']

print 'name' in d # ����ֵ����Ƿ��м�Ϊname����

#ʹ��dict()����(ͨ���ؼ��ֲ��������ֵ�)
d = dict(name = 'shihongji', age = 30)
print d

##ʹ��dict()����(ͨ��(����ֵ)���������жԴ����ֵ�
items = [('name','shibushisha'), ('age', 30)]
print items[0][0] # items[0]:���Ԫ��('name','shibushisha') items[0][0] ���:name
d = dict(items)
print d

'''

    ʹ���ֵ��ʽ���ַ���

        %s%d % ('shihongji', 1) ����ǰ���ù���ʹ��Ԫ����и�ʽ���ַ���

'''

dic = {'name':'shihongji', 'age':30}
print '%(name)s\'s age is : %(age)d' % dic



'''

    �ֵ䷽�� dic = {}

        * dic.clear() ����ڴ��е��ֵ�����,�������ø��ڴ��ֵ�ı���������� ����None

        * dic.copy() (ǳ����)  &  deepcopy(dict)(���)
            - ǳ����(copy)�����������󣬲��´��������ڲ����Ӷ���
            - ���(deepcopy)��copyģ���deepcopy��������ȫ�����˸��������Ӷ���
            - ��ϸ���Ͳο���http://blog.csdn.net/u014647208/article/details/77683545

        * dic.fromkeys() ʹ�ø����ļ������µ��ֵ䣬ÿ������Ӧ��ֵĬ��ΪNone

        * dic.get(key) �����ֵ��� ͬ dic[key]
            - ʹ��dic[key]�����ֵ��в����ڵ���ʱ�����
            - ʹ��dic.get(key)�����ֵ��в����ڵ���ʱ���������쳣���᷵��Noneֵ

        * dic.items() �����е��ֵ������б���η����磺[(����ֵ),(����ֵ)...]

        * dic.iteritems() ������items()����������ͬ�������ؽ��ʱ�����������б�iteritems()Ч�ʸ���

        * dic.keys() ���ֵ��еļ����б����ʽ�����磺[����������...]

        * dic.iterkeys() ���ֵ��еļ��Ե���������ʽ����

        * dic.values() ���б����ʽ�����ֵ��е�ֵ�磺[ֵ��ֵ��ֵ...]

        * dic.itervalues() ���ֵ��е�ֵ�Ե���������ʽ����

        * dic.pop(��) �Ƴ��ֵ��еļ�ֵ,���ر��Ƴ���Ԫ�ص�ֵ
            - �б��е�l.pop(index)������ͨ�������Ƴ��б��е�Ԫ��
            - dic.pop(��)������ͨ�����Ƴ��ֵ�Ԫ��

        * dic.popitem() ������list.pop()�Ƴ����һ��Ԫ��
            - �����ֵ��Ԫ��˳���ǹ̶��ģ�����'����Ԫ��'�ǲ��̶���
            - ���Ҫһ����һ�����Ƴ�������Ԫ�ؿ�ʹ�ô˷���

        * dic.setdefault(����Ĭ��ֵ)
            - ������趨Ĭ��ֵ������ͬget()����һ��Ĭ��ʹ��None
            - ������get()�������ܻ�ø������������ֵ
            - ���ֵ��в�������������������趨��Ӧ�ļ�ֵ
            - ����������ʱ��setdefault����Ĭ��ֵ����Ӧ�ĸ����ֵ�
            - ��������ڣ��򷵻������Ӧ��ֵ�����ٸı��ֵ��ֵ

        * dic.update(���ֵ�) ����һ���ֵ������һ���ֵ�
            - �ṩ�����ֵ��е���ᱻ��ӵ����ֵ���
            - ������ֵ��е�������ֵ��е�����ͬ�������и���
'''

# dic.clear()
d = {'name':'shihongji', 'sex':'��'}
print d
d.clear()
print d # ���{}

# dic.copy()
x = {'name':'shihongji', 'age':30}
y = x.copy()
print  y #��� {'name':'shihongji', 'age':30}

# deepcopy(dic)
from copy import deepcopy
a = {'name':'asd', 'age':20}
b = deepcopy(a)
print b #��� {'name':'asd', 'age':20}

# dic.fromkeys()
a = {}
b = a.fromkeys(['name', 'sex'])
#��ֱ��ʹ��dict�����fromkeys()����
c = dict.fromkeys(['number', 'address'])
print a, b, c #��� {} {'name': None, 'sex': None} {'number': None, 'address': None}
#�������Ĭ��ֵ����ʹ��None������ָ������Ĭ��ֵ
c = dict.fromkeys(['number', 'address'], 'defaultValue')
print c #��� {'number': 'defaultValue', 'address': 'defaultValue'}

#dic.get(key)
a = {'phone':'111', 'address':'asd'}
print a['phone'], a.get('phone') #��� 111 111
print a.get('name') #��� None
#get()���������Լ�����Ĭ��ֵ���滻None
print a.get("name", 'null') #��� null
#print a['name'] #�����ֵ���û��name�����ԣ����д���ᱨ��

#dic.items()
a = {'name':'shihongji', 'age':30}
b = a.items()
print b #��� [('age', 30), ('name', 'shihongji')]

#dic.iteritems()
b = a.iteritems()
print type(b), b #��� <type 'dictionary-itemiterator'> <dictionary-itemiterator object at 0x02A9C240>
b = list(b) #Convert the iteratir to a list(������ת�����б�)
print b, list('asdf') #��� [('age', 30), ('name', 'shihongji')] ['a', 's', 'd', 'f']

#dic.keys()
b = a.keys()
print b #��� ['age', 'name']

#dic.iterkeys()
b = a.iterkeys()
b = list(b)#Convert the iteratir to a list(������ת�����б�)
print b #��� ['age', 'name']

#dic.values()
b = a.values()
print b #[20, 'shihongji', 'boy']

#dic.itervalues()
b = a.itervalues()
b = list(b) #Convert the iteratir to a list(������ת�����б�)
print b #[30, 'shihongji']

#dic.pop()
c = a.pop('name')
print c, a #��� shihongji {'age': 30}

#dic.popitem()
a = {'url':'www.baidu.com', 'spam':0, 'title':'baidu'}
print a.popitem() # ����Ԫ�� ('url','www.baidu.com')
print a #��� {'title': 'baidu', 'spam': 0}

#dic.setdefault()
a.clear()
print a.setdefault('name') # None
print a.setdefault('sex', 'N/A') # N/A
print a.setdefault('age', 'N/A') # N/A
print a # {'age': 'N/A', 'name': None, 'sex': 'N/A'}
print a.setdefault('age', 20) # N/A (����ǰ���Ѿ�������ageĬ��ֵ���ֵ����Ѵ���age����������������û᷵�����еļ���Ӧ��ֵ�����Ҳ�������ֵ�ļ�ֵ)
print a # {'age': 'N/A', 'name': None, 'sex': 'N/A'} (age����Ӧ��ֵû�б���һ����setdefault�����޸�)
a['a'] = 'abc'
a['sex'] = 'boy'
a['age'] = 21
print a # {'a': 'abc', 'age': 21, 'name': None, 'sex': 'boy'}

#dic.update()
a.clear()
a['name'] = 'shj'
a['sex'] = 'boy'
print a # {'name': 'shj', 'sex': 'boy'}
b = {'name':'abc', 'age':20}
a.update(b)
print a # {'age': 20, 'name': 'abc', 'sex': 'boy'}
c = {'stature':170}
#����ʹ��dict���update(���ֵ䣬���ֵ�)����
dict.update(a, c)
print a, c #{'age': 20, 'stature': 170, 'name': 'abc', 'sex': 'boy'} {'stature': 170}











#------------------------------------- ������ ------------------------------------#


'''

    ���н�� ��������ֵ��

        * ���������� =  �Ҳ�ֵ�ĸ��� (x, y, z = 1, 2, 3)

            - x, y, z = 1, 2 �� x, y = 1, 2, 3 ���������쳣
'''


x, y, z = 1, 2, 3
print x, y, z

values = 4, 5, 6
print values # (4, 5, 6)
x, y, z = values
print x, y, z

x, y = y, x
print x, y

people = {'name': 'shihongji', 'age':30}
key, value = people.popitem() # popitem() �����᷵��Ԫ��
print key, value


x = y = 1
print x, y
# ͬ
y = 1
x = y
print x, y



'''

    �������ͣ�Boolean��

        * False None 0 "" () [] {} ��Ϊ�������ʽʱ����������������False
        
'''


print True == 1 # True
print False == 0 # True
print True + False + 42 # 43



'''

    bool() ����ת��
    
'''

print bool(1) # True
print bool(0) # False
print bool(0.0) # False
print bool("") # False
print bool(()) # False
print bool([]) # False
print bool(None) # False
print bool({}) # False


'''

    if ���ʽ��
        ���
    elif ���ʽ:
        ���
    else ���ʽ��
        ���

'''

a = 1

if a > 0:
    print 'a > 0'
elif a < 0:
    print 'a < 0'
else:
    print 'a == 0'


'''

    �Ƚ������

        * ==�� <�� >�� >=�� <=�� !=
        * x or y (������AS���߼�������� || )
        * x and y (������AS���߼���������� && )
        * not x  (������AS���߼�������� ��)
        * x is y (xy��ͬһ������)
        * x is not y ��xy����ͬһ������
        * x in y (x �� y�У�����֮ǰ�б��õ� a = [1,2,3] print 1 in a)
        * x not in y (x ���� y��)
        * x < > y  ��ͬ�� x != y ��������ʹ��x < > y���ַ�ʽ�����������׼���
        
'''


print 'alpha' < 'beta' # True
print [2,5] < [1,2] # False
print [2, [1, 2]] > [2, [1,6]] # False


'''

    ��Ԫ������������������

        * a if b else c (���bΪ�棬����a�����򷵻�c)
        # a = b > 0 ? 1:2 (AS��д��)
'''

name = raw_input('Please Input Your Name:')
print 'OK' if name == 'shihongji' else 'Error'


'''

    assert �ؼ��� ��Ŀǰ����⣬�պ���������

'''


'''

    ѭ�������б� for

        * ������ѭ����ʹ�����н��
'''

people = {'name':'shihongji', 'age':20}
for key in people:
    print key + ':' + str(people[key])


for key, value in people.items():
    print str(key), str(value)


# ��ӡ���ֶ�Ӧ����
names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]

# ����һ
for i in range(len(names)):
    print names[i], 'is', ages[i], 'years old'

# ������ ʹ���ڽ����� zip()
for name, age in zip(names, ages):
    print name, 'is', age, 'years old'


'''

    �ڽ�����

        * zip() ����������ѹ����һ�𣬷���һ��Ԫ����б�
            - ��������������������
            - ����Ӧ�����ȳ������У���������������ʱ��ͻ�ֹͣ

        * enumerate() ��������-ֵ��

'''

# zip()
print zip(names, ages) # [('anne', 12), ('beth', 45), ('george', 32), ('damon', 102)]

names.pop() # �Ƴ�names�е�һ��Ԫ�أ�ʹnames��agesԪ�ظ�������
print names
print zip(names, ages) # [('anne', 12), ('beth', 45), ('george', 32)]

# enumerate()
for index, name in enumerate(names):
    print 'names[', index, '] = ', name


'''

    while True/break���
    


word = raw_input('Please enter a word:')
while word:
    print 'The word was ' + word
    word = raw_input('Please enter a word:')

# ���������д�����ظ��Ĵ��� word = raw_input('Please enter a word:')
# ��ʱ����ʹ�� while True/break���

while True:
    word = raw_input('Please enter a word:')
    if not word:
        break
    print 'The word was ' + word

'''

'''

    for ѭ�� ����else

        * �������Ķ�������겢Ϊ��ʱ��λ��else���Ӿ佫ִ��
        * �����forѭ���к���breakʱ��ֱ����ֹѭ�����򲻻�ִ��else�Ӿ�

        �磺��0-9�в�������5���ҵ���ֹͣѭ�����Ҳ�������ʾû�ҵ�
'''

# ����һ ��������Ҫ����һ���Ƿ��ҵ��ı�ʶ��
founded = False

for num in range(10):
    if num == 5:
        print 'found it! num = %s' % num
        founded = True
        break;
if not founded:
    print 'not found it ...'

# ������ ʹ��forѭ������else
for i in range(10):
    if i == 5:
        print 'found it! i = %s' % i
else:
    print 'not found it ...'

# ��������ǣ�found it! i = 5
# ʵ�ʽ���ǣ�found it! i = 5 not found it ... (else ����������Ҳ�����)
# ��ȷ��д��Ӧ��Ϊ��
for i in range(10):
    if i == 5:
        print 'found it! i = %s' % i
        break # �˴�break����Ҫ
else:
    print 'not found it ...'



'''

    �б��Ƶ�ʽ

        ���������б������б��һ�ַ�����������ʽ������forѭ��

'''

print [x * x for x in range(10)] # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# ͬ

l = []
for x in range(10):
    l.append(x * x)

print l # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print [x * x for x in range(10) if x % 3 == 0] # [0, 9, 36, 81]

# ͬ

l = []
for x in range(10):
    if x % 3 == 0:
        l.append(x * x)

print l # [0, 9, 36, 81]



'''

    pass��del��exec��eval���

        * del
            - ɾ�����������ݵ����ã�����ɾ���˱�����
            - ���û�б������ô����ݣ����ᴥ�����������ڴ�
'''

x = 1
print x # 1
del x
# print x # NameError: name 'x' is not defined








#------------------------------------- ������ ------------------------------------#


'''

    ��������

        * �﷨��def func():

    ��������
    
        * �﷨��def func(x, y, z = 1, *tupleArgs, **dicArgs1)
            - *tupleArgs��Ԫ������
            - **dicArgs1���ֵ�����

'''


def func(x, y=5, *a, **b):
    print x, y, a, b

func(1) # 1 5 () {}
func(1,2) # 1 2 () {}
func(1,2,3) # 1 2 (3,) {}
func(1,2,3,4) # 1 2 (3, 4) {}
func(x=1) # 1 5 () {}
func(x=1,y=1) # 1 1 () {}
func(x=1,y=1,a=1) # 1 1 () {'a': 1}
func(y=2,x=1,a=1,b=1) # 1 2 () {'a': 1, 'b': 1}
func(1,y=1) # 1 1 () {}
func(1,2,3,4,a=1) # 1 2 (3, 4) {'a': 1}
func(1,2,3,4,k=1,t=2,o=3) # 1 2 (3, 4) {'k': 1, 't': 2, 'o': 3}



'''

    ������ת
        �������ռ�ΪԪ����ֵ������ù�������ʵ�ϣ����ʹ��*��**�Ļ�������ִ�з�����
        
'''

# ʹ��*�������
def add(x, y): return x + y

params = (1, 2)
print add(*params) # 3

# ʹ��**�����
def hello(name = 'shihongji', greeting = 'Hello'):
    print greeting, name

params = {'name':'hongji', 'greeting':'Well met'}
hello(**params)


def with_star(**kwds):
    print kwds['name'], 'is', kwds['age'], 'years old'

def without_stars(kwds):
     print kwds['name'], 'is', kwds['age'], 'years old'

args = {'name':'shihongji', 'age':20}
with_star(**args)
without_stars(args)


'''

    ʹ��ƴ�Ӳ��������ݲ��� ��Ŀǰ���Ǻ���������պ󲹳䣩

        * ���ַ�ʽ���Բ��ù��Ĳ����ĸ������ڵ��ó���Ĺ��캯��ʱ���������������

'''

def foo(x, y, z, m = 0, n = 0):
    print x, y, z, m, n


def call_foo(*args, **kwds):
    print 'Calling foo!'
    foo(*args, **kwds)




'''

    ����ע��

        * ʹ��#
        * ʹ���ĵ��ַ���
            - �ں����Ŀ�ͷд�ַ�����������Ϊ������һ���ֽ��д洢
            - �ĵ��ַ����ķ��ʷ�ʽ func.__doc__
'''


def func(x):
    'This is a func'
    return x

print func(1) # 1

print func.__doc__ # This is a func



'''

    vars()����

        * ����������Ӧ��ֵ�Ǹ����ɼ����ֵ䣬vars()�������Է��ظ��ֵ�
        
'''

ccc = 1

dic = vars()
print dic
print dic['ccc'] # 



'''

    globals()����
        * ����ȫ�ֱ������ֵ�
        * ����ֲ���������������ֺ���Ҫ���ʵ�ȫ�ֱ�������ͬ�Ļ���
            ����ʹ��globals()������ȡȫ�ֱ���ֵ

    
'''

parameter = 'berry'

def combin(parameter):
    print parameter , globals()['parameter']

combin('Shrub') # Shrub berry



'''
    �����һ����� local variable 'x' referenced before assignment ���쳣

    ԭ��
        Python������ں����ڲ���ȫ�ֱ�����ֵ���Ǹñ������Զ�תΪ�ֲ�����
        �籾�δ����� x = x + 1:
        �ں����ڸ�ȫ�ֱ���x��ֵ�����±���x�Զ�תΪ�˾ֲ�����
        x + 1��x������û�б������Ϳ�ʼʹ�ã����Իᱨ��

    �����
        ʹ��global�ں���������x��ȫ�ֱ����磺����ζ�

'''

# �����һ

'''
x = 1
def add():
    x = x + 1
    print x
add()
print x

'''

# ����ζ�

x = 1
def abcd():
    global x
    x = x + 1
    print x # 2

print x # 1
abcd()
print x # 2



'''

    Ƕ��������

        * Python�к�������Ƕ��
        * ����Ҫ��һ������������һ������ʱʹ��
        * ��㺯��������㺯��
        * ���صĺ��������Է������������ڵ�������������������ػ������ȹؾֲ�������
        * ÿ�ε�����㺯�������ڲ��ĺ������ᱻ���¶���

'''


def mul(factor):
    def mulByFactor(number):
        print factor * number
    return mulByFactor # ������㺯��mulByFactor


mbf = mul(5)
print type(mbf)
mbf(5) # 25

mul(10)(2) # 20 





#------------------------------------- ������ ------------------------------------#

'''

    ��������̣�OOP��

        * �ඨ��
            - �﷨��class ����:

'''



class Animal:

    def __init__(self):
        self.__animalType = '����'
    
    def setName(this, name):
        this.name = name

    def getName(this):
        return this.name

    def greet(this):
        print 'I\'m %s' % this.name

    def run(self):
        print 'Animal run!'

    def eat():
        print self.__animalType

cat = Animal()
dog = Animal()
cat.setName('P1')
dog.setName('P2')
cat.greet() # I'm cat
dog.greet() # I'm dog
print cat.name # cat

cat.name = 'cat1'
cat.greet() # I'm cat1

cat.age = 2
print cat.age # 2



'''

    �̳кͶ�̬

        * ��̳�
            - �﷨��class ����(����):

        *������͸��඼������ͬ��run()����ʱ������˵�������run()�����˸����run()��
        �ڴ������е�ʱ�����ǻ���������run()�����������Ǿͻ���˼̳е���һ���ô�����̬��

    ��д�����ǣ���

        �����еķ�����ͬ�����еķ�����һ��������һ��һ������ν��
    
'''


# ������û��run()����
class Cat(Animal):
    pass

class Dog(Animal):
    pass

cat = Cat()
dog = Dog()
cat.run() # Animal run!
dog.run() # Animal run!


# ��������Ӹ�����һ����run()��������ʱ����͸��������ͬ��run()����
class Cat1(Animal):
    '��������'
    def run(self):
        print 'Cat run!'

class Dog1(Animal):
    '��������'
    def run(self):
        print 'Dog run!'

cat = Cat1()
dog = Dog1()
cat.run() # Cat run!
dog.run() # Dog run!


'''

    ���಻�ܼ̳и����˽�����Ժͷ���

'''

class Monkey(Animal):

    # ����
    def climbTree():
        print 'monkey Climb Tree...'


m = Monkey()

# ��eat()�����д�ӡ__animalType���������಻�ܼ̳и���˽������
#����������������û�� __animalType ������ԣ����Իᱨ��

# m.eat() ����� TypeError: eat() takes no arguments (1 given)


'''
    * ��̬�ĺô����ǣ���������Ҫ����Dog��Cat����ʱ������ֻ��Ҫ����Animal���;Ϳ����ˣ�
    * ��ΪDog��Cat��������Animal���ͣ�Ȼ�󣬰���Animal���ͽ��в������ɡ�
    * ����Animal������run()��������ˣ�������������ͣ�ֻҪ��Animal��������࣬
    * �ͻ��Զ�����ʵ�����͵�run()����������Ƕ�̬����˼��


    * ����һ������������ֻ��Ҫ֪������Animal���ͣ�����ȷ�е�֪�����������ͣ�
    * �Ϳ��Է��ĵص���run()��������������õ�run()������������Animal��Dog����Cat�����ϣ�
    * ������ʱ�ö����ȷ�����;���������Ƕ�̬���������������÷�ֻ�ܵ��ã�����ϸ�ڣ�
    * ������������һ��Animal������ʱ��ֻҪȷ��run()������д��ȷ�����ù�ԭ���Ĵ�������ε��õġ�
    * ����������ġ����ա�ԭ��

        - ����չ���ţ���������Animal���ࣻ

        - ���޸ķ�գ�����Ҫ�޸�����Animal���͵�run_twice()�Ⱥ�����

'''

def run_twice(Animial):
    Animial.run()
    Animial.run()
    print

run_twice(Cat1()) # Cat run! Cat run!
run_twice(Dog1()) # Dog run! Dog run!


'''

    __new__()��

        * ���󴴽�ʱ���ȵ��� __new__() ���캯�����ɶ���
        Ȼ�����__init__(self)������ʼ������

    ��ʼ������ �� __init__(self)

        * ����__init__�������ڴ���ʵ����ʱ�򣬾Ͳ��ܴ���յĲ����ˣ�
        * ���봫����__init__����ƥ��Ĳ�������self����Ҫ��

    ˽�б��� �� __������ �������˫�»��ߣ�

    ˽�б������ʷ�ʽ��

        * ��˽�б�����Ӷ����get��set����
        * �磺����__sex
        * set_sex(self, value) �� get_sex(self)



    ˽�к����� __������() (ͬ˽�б���һ��������˫�»��Q��ͷ)
    
'''


class Student():
    def __init__(self, name, score, sex):
        self.name = name
        self.score = score
        self.__sex = sex

    def set_sex1(self, sex):
        self.__sex = sex

    def get_sex(self):
        return self.__sex

    def __sayHello(self):
        print('sayHello')

    def print_studentInfo(self):      
        print '%s is a %s, thie score is : %s' % (self.name, self.__sex, self.score)

stu = Student('xiaoming', '59', 'boy')
stu.print_studentInfo() # xiaoming : 59

stu.set_sex1('girl') # ������sex��˽�б��� ������ʹ��stu.__sex��ʽ���и�ֵ
stu.print_studentInfo()

# stu.__sayHello() �ⲿ�ǲ��ܵ���˽�к�����

print stu.get_sex()



'''

    __str__(self):

        * ������ӡ������Ϣ

        * һ��Ҫ�з���ֵ

'''

class Car():

    def __init__(self, name, color):
        self.name = name
        self.color = color

    # ��д __str__(self)
    
    def __str__(self):
        return 'name : %s, color : %s' % (self.name, self.color)
        

car = Car('����', '��ɫ')

# ������뿴�������Ľ��(�ڴ��ַ)��<__main__.Car instance at 0x02822580>

# ����д __str__(self) ����� name : ����, color : ��ɫ

print(car) 



'''

    ���á���ȡ�������Ժͼ�����ĳ�����Ƿ����
    
        * hasattr()
        * setattr()
        * getattr()

'''

print hasattr(stu, 'height') # False
setattr(stu, 'height', '170') 
print stu.height # 170
print getattr(stu, 'height') #170




'''

    ��ȡ�������Ϣ

        * type()
        * isinstance()
        * dir()
            - ���һ��������������Ժͷ�����������һ�������ַ�����list
        * issubclass(���࣬ ����)
            - ���һ�����ǲ�����һ���������

'''


print type('123') # <type 'str'>
print type(cat) # <type 'instance'>
print type(dog) # <type 'instance'>
print type(Animal) # <type 'classobj'>
print isinstance(cat, Cat) # False
print isinstance(cat, Animal) # True
print dir(Animal) # ['__doc__', '__module__', 'getName', 'greet', 'run', 'setName']
print Cat1.__doc__ # ��������
print issubclass(Cat1, Animal) # True
print issubclass(Animal, Cat1) # False



'''

    �����ʵ����̬�����Ժͷ���

'''

# ��ͨ������
class vehicle:
    pass

ve = vehicle()
ve.speed = 100 # ��̬��speed����
print ve.speed # 100

# ���������һ������
def run(self):
    print 'running'

# ��ʵ��ve��run����
from types import MethodType
ve.run = MethodType(run, ve, vehicle)
ve.run()



'''


    ʹ��__slots__

        * �������ʱ����һ�������__slots__�������������Ƹ�������ӵ�����,
        �൱��java��c++�еĳ�Ա��������
            - ���磺ֻ�����vehicle2��ʵ�����speed��color����

        * __slots__���������ǣ������ڴ�������ʵ����ʱ����ӽ�ʡ�ڴ档
    
'''


# �����ԣ���Ҫ�̳�object ʹ��__slots__�Ż���Ч
class vehicle2(object):
    __slots__ = ('speed', 'color')


ve2 = vehicle2()
ve2.speed = 100
ve2.color = 'white'
print ve2.speed # 100
print ve2.color # white
# ve2.price = 2780 # AttributeError: 'vehice2' object has no attribute 'price'

#__slots__��������Խ��Ե�ǰ�������ã��Լ̳е������ǲ�������
#car����Ȼ�̳���vehicle2�࣬����û��ʹ��__slots__���ԣ�����car��ʵ�����԰�price����
class car(vehicle2):
    pass

c = car()
c.price = 2000
print 'car\'s price is:', c.price # car's price is: 2000



# ������������Ҳ����__slots__����������������������Ծ��������__slots__���ϸ����__slots__
class bike(vehicle2):
    __slots__ = ('name', 'price')


b = bike()
b.price = 1000
b.name = 'dasanba'
b.speed = 100
b.color = 'black'
print b.price, b.name, b.speed, b.color # 1000 dasanba 100 black
# b.size = 1890 # AttributeError: 'bike' object has no attribute 'size'




'''

    ʹ��@property

        * Python���õ�@propertyװ�������Ǹ����һ������������Ե��õ�
'''


# �����������Ը�ֵ��ȡֵ�ķ�ʽ
class point:
    def set_x(self, x):
        self.x = x

    def get_x(self):
        return self.x

p = point()
p.set_x(10)
print 'X:', p.get_x() # X:10


# ʹ��@property�ķ�ʽ
class point2:
    
    @property
    def x(slef):
        return self.x    

    @x.setter
    def x(self, x):
        self.x = x

p2 = point2()
p2.x = 20
print 'p2.x :', p2.x # p2.x : 20



'''

    ���ؼ̳�

        * �﷨��class ����(���࣬��Mixin...)

        * ͨ�����ؼ̳У�һ������Ϳ���ͬʱ��ö����������й��ܡ�


    Mixin���

        * ��ʾ����(mix-in)�������߱��ˣ����������Ϊ������ӵ������У���������Ϊ����

    ʹ��Mixin��ʵ�ֶ��ؼ̳�Ҫ�ǳ�С��
    
        * �����������ʾĳһ�ֹ��ܣ�������ĳ����Ʒ����ͬJava�е�Runnable��Callable��
        * ������������ε�һ������ж�����ܣ��Ǿ�д���Mixin��
        * Ȼ�����������������ʵ��
        * ������༴��û�м̳����Mixin�࣬Ҳ�������Թ���������ȱ����ĳ�����ܡ�

    �����Airplane��ʵ���˶�̳У��������̳еĵڶ�������������ΪPlaneMixin��
    ������Plane���������Ӱ�칦�ܣ����ǻ���ߺ�����������ˣ��������һ��Mixin�ࡣ
    ���ԴӺ�������⣬Airplaneֻ��һ��Vehicle������һ��Plane��
'''

class Vehicle(object):
    pass
 
class PlaneMixin(object):
    def fly(self):
        print 'I am flying'
 
class Airplane(Vehicle, PlaneMixin):
    pass



'''

    Python�л���һ���������Ԫ��ĸ���ݲ����ף��պ󲹳䣩

'''





#------------------------------------- �ڰ��� ------------------------------------#


'''

    �쳣
        �﷨��
        
            try:
                pass
            except:
                pass
            finally:
                pass

    Python���еĴ����Ǵ�BaseException�������ģ������Ĵ������ͺͼ̳й�ϵ�����
    https://docs.python.org/2/library/exceptions.html#exception-hierarchy

    
'''


try:
    print 10 / 0
except Exception, e:
    print e
finally:
    print 'finally...'


'''

    �������û�б��������ͻ�һֱ�����ף����Python���������񣬴�ӡһ��������Ϣ��Ȼ������˳���

    ������ʵ����

    def foo(s):
        return 10 / int(s)

    def bar(s):
        return foo(s) * 2

    def main():
        bar('0')


    main()


'''




'''

    ��¼����

        * Python���õ�loggingģ����Էǳ����׵ؼ�¼������Ϣ

        * ͨ�����ã�logging�����԰Ѵ����¼����־�ļ���

        

    ��������ͬ���ǳ����������ӡ�������Ϣ������ִ�У��������˳���

'''

import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except StandardError, e:
        logging.exception(e)

main()
print 'END'



'''

    �Զ����쳣��

        �﷨��
            class CustomException(Exception): pass
            
        * ��������һ����ֻҪȷ����Exception��̳У������Ǽ�ӻ���ֱ�ӵģ�����˵�̳��������ڽ��쳣��Ҳ���ԣ�

'''


'''

    ���Except

'''

try:
    x = input('Enter the first number: ')
    y = input('Enter the second number: ')
    print  x / y

except ZeroDivisionError:
    print 'ZeroDivisionError...'

except TypeError:
    print 'TypeError...'

# ��

except (ZeroDivisionError, TypeError):
    print 'Error Message...'


'''

    ��ȡ�쳣�Ķ���e

'''
try:
    print 1 / 0

except (ZeroDivisionError, TypeError), e:
    print 'Error Message: ', e




'''

    ��try/except���else���

        �﷨��
            try:
            except:
            else:
            finally:

        * else�е����ֻ����û���쳣������ʱ��Ż�ִ��

        ����ʾ����

            * ���벻��ȷ�����쳣������ͻ᲻��Ҫ������
            * ������ȷû���쳣���ͻ�ִ��else�е���䣬��������

'''


while True:
    try:
        x = input('Enter the first number: ')
        y = input('Enter the second number: ')
        print  x / y
        
    except:
        print 'Invalid input,please try again!'

    else:
        break

    finally:
        print 'exec finally...'


'''

    raise�ؼ���

        * ���쳣�����ϲ���ô�

'''

def cacl():
    try:
        print 1 / 0
    
    except:
        raise Exception('Something is wrong!') # �Ӵ˴��׳��쳣����Ƕ���



def exec_cacl():
    cacl() # ��Ƕ� �˴����쳣�����������������


# exec_cacl() # ����� �˴��쳣δ����������ǿ����ֹ

# ������������exec_cacl����������쳣��׽�Ż�����
# ����׽���쳣�󣬻��������ִ�У�����ǿ����ֹ����
try:
    exec_cacl()

except Exception, e:
    print 'exec_cacl errorInfo: ', e


print 'END!'







#------------------------------------- �ھ��� ------------------------------------#


'''

    �󶨷�����δ�󶨷���

        * ������ķ������Ƿǰ󶨷��������������÷�������ʵ������ķ������ǰ󶨵ģ������ʵ�����÷�����

        �ο���http://blog.csdn.net/qin_shang_/article/details/79013420


    ���ó���ķǰ󶨷���

        * parents.__init__(this) (����ʹ��)
        
        * super(child1, this).__init__() (�Ƽ�ʹ��)

        super()��ϸ�ο���
        http://blog.csdn.net/mashijia986/article/details/79126287
'''


from random import randint

class parents(object):
    def __init__(this):
        this.xx = randint(1,10)
        this.yy = randint(1,10)

    def cacl(this):
        print 'x / y = %.1f' % (this.xx / this.yy)

    def printString(this):
        print 'printString...'

class child(parents):
    def __init__(this):
        pass

# ����ʵ��ֱ�ӵ���cacl����û������
p = parents()
p.cacl() # x / y = 1.0

# ����ʵ�����ø����еķ���
c = child()
c.printString() # printString...

# ��Ϊcacl������ʹ�õ�xx��yy�����ԣ��������������cacl����ʱ������û�б���ʼ����
# ���Ա���xx��yy����û�б�����
# ����취�� ����δ�󶨵ĸ��෽��
try:
    c.cacl() 
except Exception, e:
    print e # AttributeError: 'child' object has no attribute 'xx'
 

# ���������뱨�����⣺   ����δ�󶨵ĸ��෽��

class child1(parents):
    def __init__(this):
        
       # parents.__init__(this) # ����ʹ�����ַ���
       
       # ��ʹ��
       
       super(child1, this).__init__() # �Ƽ�ʹ�����ַ���

c1 = child1()
c1.cacl() # x / y = 1.0





'''

    ��̬���������Ա����

        * ��̬���������Ա�����ڴ���ʱ�ֱ�װ��Stticmethod���ͺ�Classmethod���͵Ķ�����

    ��̬����

        * staticmethod

        * ����Ҫself���������Ա��౾��ֱ�ӵ���


    ���Ա����

        * classmethod

        * �����ڶ����ʱ����Ҫ��Ϊcls��������self�Ĳ���


    װ����

        * ʹ��@������

        * @staticmethod  @classmethod

    
'''


class MyClass:

    @staticmethod
    def smeth():
        print 'This is a static method'

    @classmethod
    def cmeth(cls):
        print 'This is a class method of', cls


MyClass.smeth()

# ���Ա��������ֱ������ľ��������ã���cls�������Զ����󶨵����
# ����һ��ֱ��ʹ�� MyClass.cmeth()
MyClass.cmeth()


'''

    �������ݲ��˽�

'''




#------------------------------------- ��ʮ�� ------------------------------------#



'''

    ģ�鶨��

        * Ϊ�˴���������

    ����������һ��hello.py���ļ���������e:/PythonSpaceĿ¼��

    ��������Ǹ��߽�������������ģ��
    
'''

import sys
sys.path.append('e:/PythonSpace')

'''

    ����ģ��

        * ����ģ���κ͵���һ��Ч����һ����
    
'''


import HellloWorld


'''

     ģ�����¼��� �� �����ܱ�����������

        * reload(ģ����)

'''

# helloģ���Ѿ���������һ�Σ�����ͨ��reload�����ķ���ֵ����hello
# ��������İ汾�滻����һ�ε���İ汾
HellloWorld = reload(HellloWorld)


'''

    __name__����
    
        * ��������(��ǰִ�еĳ���)��ʹ��ʱ��__name__��ֵ��'__main__'
        * ����ǵ����ģ�飬���ֵ�ͱ��趨Ϊģ�������
'''

print __name__ # '__main__'

print HellloWorld.__name__ # HellloWorld

print sys.path

from Hello2 import hello
hello()


import drawing
from drawing import color

color.test()

print range.__doc__


'''

    ��׼��

        * Python�а�����һЩģ�飬�ܳ�Ϊ��׼��

        * �򵥽���һ����

            - sys ͨ����ģ����Է��ʶ����Python�����������ܵı����ͺ���

            - os ͨ����ģ����Է��ʵ�����Ͳ���ϵͳ��ϵ���ܵı����ͺ���

            - fileiput ͨ����ģ��������ɱ�������ļ������е�������

            - sets��heapq��deque ������ģ���ṩ��3�����õ����ݽṹ��
                . ����Ҳ���ڽ�������set����

            - time ͨ����ģ����Ի�ȡ��ǰʱ�䣬 �����Խ���ʱ�����ڲ����͸�ʽ��

            - random ��ģ���еĺ������Բ������������������ѡȡ���Ԫ���Լ������б�Ԫ��

            - shelve ����������ӳ�䣬ͬʱ��ӳ������ݱ����ڸ����ļ��������ݿ���

            - re ֧��������ʽģ��
    
'''



#------------------------------------- ��ʮһ�� ------------------------------------#



'''

    �ļ���д

        open����

            * open(name[, mode[, buffering]])
'''

help(open)

print open.__doc__

f = open('somefile.txt', 'w')

# ÿ�ε���f.write()��ʱ�����ݶ�����׷�ӵķ�ʽд���ļ���
f.write('Hello')
f.write('World')

f.close()


f = open('somefile.txt', 'r')

# ��5���ֽڵ��ַ�
print f.read(5) # Hello

# ��ȡʣ����ַ�
print f.read() # World

f.close()


'''
    read([bytes])

        * ����ָ����ȡ���ֽ���

        * ���ļ�ָ�����ڵ�λ�ã������ļ���β(�������ָ�����ֽ���)

    readline([bytes]) - ��ȡһ��

        * ����ָ����ȡ���ֽ���

        * ���ļ�ָ������λ��һֱ�����з����֣�����ͬ���з�һ�������

    readlines() - ��ȡ�ļ��е������У����ҽ�����Ϊ�б���
    

    writelines(�б�) - ���ļ���д���������

        * ͬreadlines()�෴��������һ���ַ����б�

        * û��writeline()������ֻ��ʹ��write

'''


f = open('somefile.txt', 'w');
f.write("hello shihongji\n")
f.write('hello shihonghong')
f.close()

f = open('somefile.txt', 'r')
print f.read() # hello shihongjihello shihonghong ��ȡ�ļ��������ı�
print f.readline() #����ִ����f.read(),��ʱָ���Ѿ������ļ�ĩβ,���Բ��ܶ�ȡ���ı�
f.seek(0) # ��ָ��ָ���ļ���ͷ
print  f.readline(5) # hello ��ȡ5���ֽ�
print  f.readline() #  shihongji
print f.readlines() # ['hello shihonghong'] �ڵ�ǰ�α��λ�ö�ȡ
f.seek(0)
print f.readlines() # ['hello shihongji\n', 'hello shihonghong']

f.close()

f = open('somefile.txt', 'w')
f.writelines(["write", "lines"])
f.close()

raw_input("123") # ͨ���ȴ��������ó�����ͣ, �鿴�ļ��е�����

'''

    �ܵ����

        * sys.stdout ��׼���, ��Ӧ�Ĳ�������print����ӡ��

            - print 1
            
            - ��Ч���ǰ� 1 д��console�������У��������㿴
            - ʵ�������Ĳ����������Ϊ����console�������У���Ϊһ�����ӣ�
            ͨ��sys.stdout = consoleָ����console������д����(console ��Ĭ�ϵģ�
            Ҳ����˵�㲻�޸�Ҫ���Ķ�д�Ļ����ͻ�Ĭ������д)����print 1��ʱ��
            ���Ǹ���python����Ҫд1��Ȼ��python�ͻ�ȥsys.stdout��ָ���İ����
            Ҳ����console�������У���д�� 1��
            -����׼�������Ҳ��ͬ���Ĺ��̣���ᷢ�ֵ��������ʱ��������ϢҲ���ӡ��console���档
            - ��ʵֻҪһ���������write�������Ϳ��Ա����������ӡ�������sys.stdoutȥ����д��
            - ˵��write��������һ���뵽�Ŀ��ܾ����ļ�������

            
        
        * sys.stdin ��׼���룬 ���Ӧinput���������룩����

            - �߼�ͬsys.stdoutһ����Ĭ�ϵİ��Ӷ���concole(������)
            - ֻҪһ���������write�������Ϳ��Ա����������ӡ�������sys.stdoutȥ�������

        * sys.stderr ��׼��������� �ͱ�׼�������Ҳ��print����ӡ��


        �ο� http://www.cnblogs.com/turtle-fly/p/3280519.html
        
'''


import sys

# ���ļ�������write()�������Ϳ��Ա�����������׼����ͱ�׼��������İ���
f = open('somefile.txt', 'w')
__console__ = sys.stdout # ��Ĭ�ϵİ��ӣ������У���һ�����ݣ��Ա��ٸĻ���

sys.stdout = f

print 123456789 # ������ļ���

f.close() # һ��Ҫ�ǵùر��ļ�

sys.stdout = __console__ # �Ѱ������»���console(����̨)

print 2 # ���������̨






'''

    sys.stdin.read() & sys.stdin.readline()

        * sys.stdin ��������д����

        * sys.stdin.read() & sys.stdin.readline() ��д�ڰ����ϵ����ݶ�����

        * sys.stdin.read()���Խ��ܶ��еı�׼����,��ȡ���� ctrl+d�ǽ������� ��enter�ǻ��С�

        * sys.stdin.readline() ��������һ�е�ȫ������,�Ὣ��׼����ȫ����ȡ��
            ����ĩβ��'\n'�������len���㳤��ʱ�ǰѻ��з�'\n'���ȥ�˵�

    raw_input �� sys.stdin.readline()����
    
        * raw_input()��ȡ����ʱ���صĽ���ǲ�����ĩβ�Ļ��з�'\n'��

        * sys.stdin.readline() ��ȡ�Ľ���а���ĩβ�Ļ��з�'\n'


    strip('\n')

        * ȥ����ȡ�������Ļ��з� sys.stdin.readline().strip('\n')
    
'''

text = sys.stdin.read()
print 'sys.stdin.read: ', text


text = sys.stdin.readline()
print 'sys.stdin.readline = ', text


text1 = sys.stdin.readline()
print 'sys.stdin.readline.len = ', len(text1)


text2 = sys.stdin.readline().strip('\n')
print 'sys.stdin.readline.strip.len = ', len(text2)


'''

    seek(offset[, whence])

        * ���������ƶ��ļ���ȡָ�뵽ָ��λ�á�

        * offset -- ��ʼ��ƫ������Ҳ���Ǵ�����Ҫ�ƶ�ƫ�Ƶ��ֽ���

        * whence��
            - ��offset����һ�����壬��ʾҪ���ĸ�λ�ÿ�ʼƫ��
            - ��ѡ��Ĭ��ֵΪ 0
            - 0������ļ���ͷ��ʼ����
            - 1����ӵ�ǰλ�ÿ�ʼ����
            - 2������ļ�ĩβ����

            
    tell()

        * ���������ļ��ĵ�ǰλ�ã����ļ�ָ�뵱ǰλ��

'''

x =file('a.txt','w+')
x.write('aaaaaaaaaa') # ���ļ���д10��a

print x.tell()      # 10 ��ʾ������ǰ�α����ļ�ĩβ

x.seek(3)    # �ƶ�3���ֽڣ�whenceû������Ĭ��Ϊ���ļ���ͷ��ʼ
print x.tell() # 3

x.seek(5,1)  # �ƶ�5���ֽڣ�1����ӵ�ǰλ�ÿ�ʼ
print x.tell() # 8 �ӵ�ǰ�α�����λ���ƶ�5���ֽ�

x.seek(-1,2)# ��ǰ�ƶ�1���ֽڣ�2������ļ�ĩβ��ʼ
print x.tell()

print x.readline() # a


'''

    f.flush()

        * �����ݴ洢�ڻ����У�ֱ���ر��ļ��Żᱻд���ļ��������Ҫ����ʹ���ļ������ر��ļ���
            - �����ϸ�ļ����ݣ�����flush()�������ɻ����е�����д���ļ���

'''



'''

    fileinput() - �������ļ�ʱʹ��

        * ʹ��ʱ��Ҫ����fileinputģ��

        * fileinput.input(filename)��ģ���input()����ͬreadlines()�������ƣ�
            ����input()ÿ��ֻ����һ�е�������
'''

import fileinput

for line in fileinput.input('a.txt'):
    print line






