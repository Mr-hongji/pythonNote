'''

    了解城市代码的抓取过程，有助于对网页抓取有更深理解
    
'''

import urllib2

url = 'http://m.weather.com.cn/data3/city.xml'

content = urllib2.urlopen(url).read()

print content

