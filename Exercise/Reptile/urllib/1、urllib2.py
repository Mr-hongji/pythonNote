# -*- coding:utf-8 -*-
''''''

import urllib2, urllib


def urllib2_urlopen():

    # 向指定的url地址发送请求，并返回服务器响应的类文件（类似文件）对象
    response = urllib2.urlopen("http://www.baidu.com/")

    # 服务器返回的类文件对象支持Python文件对象的操作方法
    # read()方法就是读取文件里的全部内容，返回字符串
    html = response.read()

    # 打印响应内容
    print html


'''
urllib2.Request（url [，data] [，headers] [，origin_req_host] [，unverifiable]）
    
'''

def urllib2_request():

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
    }

    # 通过urllib2.Request() 方法构造一个请求对象
    request = urllib2.Request("http://www.baidu.com/", headers=headers)

    response = urllib2.urlopen(request)

    html = response.read()

    # 返回 HTTP的响应码，成功返回200，4 服务器页面出错，5 服务器问题
    print response.getcode()

    # 返回 实际数据的实际URL，防止重定向问题
    print response.geturl()

    # 返回 返回服务器响应的HTTP报头
    print response.info()

    # 打印响应内容
    # print html



'''
urllib.urlencode(字典)

    当请求的url的参数中有中文，需要将参数以urlencode的格式传输
    
'''

def urllib_urlencode():

    wd = {'wd':'百度 你好'}
    # urlencode()方法的参数是一个字典
    encodeResult = urllib.urlencode(wd)

    print(encodeResult)  # 输出 wd=%E7%99%BE%E5%BA%A6

    response = urllib2.urlopen('http://www.baidu.com/s?' + encodeResult)

    print(response.read())

urllib_urlencode()