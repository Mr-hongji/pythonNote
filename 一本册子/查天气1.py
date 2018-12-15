'''

    查天气

        * 利用天气网提供的接口需查询出城市的代码
        * 使用查询处的城市代码请求天气网的接口接收城市天气数据
        * http://www.weather.com.cn/data/cityinfo/城市代码.html
        

    urllib2：

        * 用来发送网络请求，获取数据

    json:
    
        * data = json.loads(content) json字符串转成字典

    type:
        * print type(data) 查看对象类型
'''

from city import city

import json
import urllib2

'''

    解决编码问题

'''


#web = urllib2.urlopen('http://www.baidu.com')

#content = web.read() #读出网站内容

#print content



cityname = raw_input('您要查询那个城市的天气？\n')

citycode = city.get(cityname)

print citycode

if citycode is None:
    
    print '没有找到该城市！'

else:

    url = 'http://www.weather.com.cn/data/cityinfo/%s.html' % citycode

    print url

    content = urllib2.urlopen(url).read()

    print content

    weatherdata = json.loads(content) ############## json字符串转成字典 ##################

    print type(weatherdata)

    weatherinfo = weatherdata['weatherinfo']

    print '\n' + cityname # weatherinfo['weather'],weatherinfo['temp1'],weatherinfo['temp2']
        
    print  '%s\n%s ~ %s' % (weatherinfo['weather'],weatherinfo['temp1'],weatherinfo['temp2'])

    
   # try:
        
        
    #except:

       # print '信息查询失败！'
        
