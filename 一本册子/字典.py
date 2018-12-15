'''

    字典（dictionary）
    
        * 是一个键/值对的集合
'''

score = {} #创建一个空字典


score = {'萧峰': 95, '段誉': 97, '虚竹': 89}

print score['段誉']


for name in score:
   print score[name]


score['段誉'] = 100 #修改数据
print score['段誉']


score['慕容复'] = 88  #向字典中添加一条数据

print score['慕容复']


del score['萧峰'] # 删除数据
