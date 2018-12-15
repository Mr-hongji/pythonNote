'''

    从文件中读取数据，统计每个人的总成绩

'''

f = file('scores.txt')
datas = f.readlines()
f.close()

result = []

for data in datas:
    l = data.split()
    sumScore = 0
    for score in l[1:]:
        sumScore += int(score)
    print l[0]+': '+ str(sumScore)
    result.append(l[0]+': '+ str(sumScore))


wf = file('result.txt', 'w')
wf.writelines(result)   #注意：因为result是个数组，在写文件的时候需要使用writelines()
wf.close
