# -*- coding:utf-8 -*-
'''

知识点：


    1、使用 BeautifulSoup4 获取页面元素的属性值

        BeautifulSoup4 和 XPath、正则 一样，都是解析 HTML 页面标签的

        BeautifulSoup4 DOC 地址：
            http://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#css

'''

'''

    目前没有弄明白 csdn 登录时，需要 fkid 参数的生成规则，不能登录成功

'''

import  requests, urllib
from bs4 import BeautifulSoup

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

login_page_url = 'https://passport.csdn.net/account/login'

requestLoginURL = 'https://passport.csdn.net/account/verify'

validateCode = None # 'https://passport.csdn.net/ajax/verifyhandler.ashx?rand=15335246503.99'

data = {

    'gps': '',
    'username': 'shihongji',
    'password': 'shihongji?!A25999',
    'rememberMe': 'true',
    'fkid': 'WHJMrwNw1k%2FEuGoY2Q2xsv4m043kwn2XYKIht1yXfFBjl6ZDWBPU9RZdE%2Bw522aJIRnbszZ18j%2FEP1HtpwU301YlfjxzEfEvOcBr9yySjCSTGaNpm6Xiy%2FpSD3EmPbcN1b2GXgZ5AQVIfxIfhRz7ENR%2Fww9utkHZcKyFCar%2BkROpkhoMiJ81hY2VkDSP4LI5G1S42CNvpqsMRTkAd7H%2FeWl9H8wGaTIOPOzDtm8KVrsWEfhZtCt1hcpn8hbF3LrabBYP2DI4NDfEEy5HbCBhxDd4A3puZnmpP1487582755342',
    '_eventId':'submit'
}

# 使用 requests 的 session 登录
se = requests.session()

response = se.get(login_page_url, headers = header, verify = False)

html = response.text
print(html)

# 以lxml 方式解析 HTML 内容
bfs = BeautifulSoup(html, 'lxml')

# 获取 name 是 lt 的 input 元素中的 value 值
lt = bfs.find('input',attrs={'name':'lt'}).get('value')
execution = bfs.find('input',attrs={'name':'execution'}).get('value')

data['lt'] = lt
data['execution'] = execution


yanzheng_img = bfs.find('img', attrs={'id':'yanzheng'})

if yanzheng_img:
    yanzheng =  yanzheng_img.get('src')

    res_yanzheng = requests.get(yanzheng, headers = header, verify = False)
    with open('d:/yanzheng.png','wb') as f:
        f.write(res_yanzheng. text)

    validateCode = raw_input('请输入验证码：')

    data['validateCode'] = validateCode


response = se.post(requestLoginURL, urllib.urlencode(data), headers = header, verify = False)

html = response.text

print(html)