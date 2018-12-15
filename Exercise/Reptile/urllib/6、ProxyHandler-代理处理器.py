# -*- coding:utf-8 -*-
'''

代理控制器

    免费短期代理网站：

        1、西刺代理 http://www.xicidaili.com/
        2、快代理 https://www.kuaidaili.com/free/
        3、360代理IP http://www.swei360.com/



    使用代理返回的数据可能会有乱码，是因为代理服务的编码格式和本地不一致，使用 str.decode（编码格式）一下就好

'''

import urllib2

def proxyHandlerTestFunc1():
    # 代理开关
    proxySwitch = True

    # 有代理的控制器 {协议头：IP：端口}
    # 如果是自己买的的私有IP代理会有用户名和密码,使用时需要使用用户名 和 密码授权才可以
    # 格式为 {协议头：用户名：密码@IP：端口}
    # 例： {'http':'hongji:mima@219.141.153.3:80'}
    # 如果使用的是私密代理的时候，代理中没有拼接用户名和密码，则会报  HTTP 407 错误，表示代理没有通过身份验证：
    # urllib2.HTTPError: HTTP Error 407: Proxy Authentication Required
    # 私密代理身份验证有两种方式：
    # 一、直接拼接用户名和密码： {'http':'hongji:mima@219.141.153.3:80'}
    # 二、使用密码管理器 HTTPPasswordMgrWithDefaultRealm() 方法
    proxy_handler = urllib2.ProxyHandler({'http':'219.141.153.3:80'})

    # 没有代理的控制器
    nullproxy_handler = urllib2.ProxyHandler()

    if proxySwitch:
        opener = urllib2.build_opener(proxy_handler)
    else:
        opener = urllib2.build_opener(nullproxy_handler)


    request = urllib2.Request('http://www.baidu.com/')

    response = opener.open(request)

    print(response.read())

    # 这么写，就是将opener应用到全局，之后所有的，不管是opener.open()还是urlopen() 发送请求，都将使用自定义代理。
    # 设置全局的控制器，可以让 urlopen() 方法使用这个opener，而不是用urlopen中自带的opener
    # 这个时候就可以直接使用 urllib2.urlopen() 这个方法
    urllib2.install_opener(opener)

    res = urllib2.urlopen(request)

    print(res.read())





'''

如果代理IP足够多，就可以像随机获取User-Agent一样，随机选择一个代理去访问网站。

'''

import random

def proxyHandlerTestFunc2():

    proxy_list = [
        {"http" : "124.88.67.81:80"},
        {"http" : "124.88.67.81:80"},
        {"http" : "124.88.67.81:80"},
        {"http" : "124.88.67.81:80"},
        {"http" : "124.88.67.81:80"}
    ]

    # 随机选择一个代理
    proxy = random.choice(proxy_list)

    # 使用选择的代理构建代理处理器对象
    httpproxy_handler = urllib2.ProxyHandler(proxy)

    opener = urllib2.build_opener(httpproxy_handler)

    request = urllib2.Request("http://www.baidu.com/")
    response = opener.open(request)
    print response.read()


