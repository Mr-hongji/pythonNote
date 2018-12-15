# -*- coding:utf-8 -*-
'''

父类：HTTPPasswordMgr（Manager）：密码管理

子类：HTTPPasswordMgrWithDefaultRealm ： WithDefaultRealm（指定默认的域）与代理服务器相关

class HTTPPasswordMgrWithDefaultRealm(HTTPPasswordMgr)


HTTPPasswordMgrWithDefaultRealm()类将创建一个密码管理对象，用来保存 HTTP 请求相关的用户名和密码，主要应用两个场景：

    1、验证代理授权的用户名和密码 (ProxyBasicAuthHandler()代理授权处理器)
    2、验证Web客户端的用户名和密码 (HTTPBasicAuthHandler()验证Web客户端的授权处理器)

ProxyBasicAuthHandler(代理授权验证)

    * 如果我们使用之前的代码来使用私密代理，会报 HTTP 407 错误，表示代理没有通过身份验证：
    urllib2.HTTPError: HTTP Error 407: Proxy Authentication Required


所以我们需要改写代码，通过：

HTTPPasswordMgrWithDefaultRealm()：来保存私密代理的用户密码
ProxyBasicAuthHandler()：来处理代理的身份验证。

'''


import urllib2,urllib


'''
ProxyBasicAuthHandler

    处理代理验证处理器方法

    使用代理抓取百度首页

    除了使用这种方式 还可以使用之前的 ProxyHandler({'http': '用户名：密码@代理IP：端口'})来做

'''


def ProxyBasicAuthHandlerFunc():

    # 私密代理授权的账户
    user = "mr_mao_hacker"
    # 私密代理授权的密码
    passwd = "sffqry9r"
    # 私密代理 IP
    proxyserver = "61.158.163.130:16816"

    # 1. 构建一个密码管理对象，用来保存需要处理的用户名和密码
    passwdmgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

    # 2. 添加账户信息，第一个参数realm是与远程服务器相关的域信息，一般没人管它都是写None，后面三个参数分别是 代理服务器、用户名、密码
    passwdmgr.add_password(None, proxyserver, user, passwd)

    # 3. 构建一个代理基础用户名/密码验证的ProxyBasicAuthHandler处理器对象，参数是创建的密码管理对象
    #   注意，这里不再使用普通ProxyHandler类了
    proxyauth_handler = urllib2.ProxyBasicAuthHandler(passwdmgr)

    # 4. 通过 build_opener()方法使用这些代理Handler对象，创建自定义opener对象，参数包括构建的 proxy_handler 和 proxyauth_handler
    opener = urllib2.build_opener(proxyauth_handler)

    # 5. 构造Request 请求
    request = urllib2.Request("http://www.baidu.com/")

    # 6. 使用自定义opener发送请求
    response = opener.open(request)

    # 7. 打印响应内容
    print response.read()




'''

HTTPBasicAuthHandler处理器（Web客户端授权验证）


有些Web服务器（包括HTTP/FTP等）访问时，需要进行用户身份验证(如小能的 kehu.ntalker.com)，爬虫直接访问会报HTTP 401 错误，表示访问身份未经授权：

urllib2.HTTPError: HTTP Error 401: Unauthorized

如果我们有客户端的用户名和密码，我们可以通过下面的方法去访问爬取：

'''

def HttpBasicAuthHandlerFunc():

    '''
        在访问 kehu.ntalker.com/ 的时候需要输入用户名和密码 使用 HTTPPasswordMgrWithDefaultRealm 密码管理类
        来实现自动登录   kehu.ntalker.com/
    '''

    # 登录 kehu.ntalker.com 的用户名
    user = 'admin'
    # 登录 kehu.ntalker.com 的密码
    passwd = 'd2a381777ea8'
    # Web服务器 IP
    webserver = '192.168.30.242'

    header = {
        'Host': 'kehu.ntalker.com',

        'User - Agent': 'Mozilla / 5.0(Windows NT 6.1;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 67.0.3396.99Safari / 537.36'

    }

    # 1. 构建一个密码管理对象，用来保存需要处理的用户名和密码
    passwdmgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

    # 2. 添加账户信息，第一个参数realm是与远程服务器相关的域信息，一般没人管它都是写None，后面三个参数分别是 Web服务器、用户名、密码
    passwdmgr.add_password(None, webserver, user, passwd)

    # 3. 构建一个HTTP基础用户名/密码验证的HTTPBasicAuthHandler处理器对象，参数是创建的密码管理对象
    httpauth_handler = urllib2.HTTPBasicAuthHandler(passwdmgr)

    # 4. 通过 build_opener()方法使用这些代理Handler对象，创建自定义opener对象，参数包括构建的 proxy_handler
    opener = urllib2.build_opener(httpauth_handler)

    # 5. 可以选择通过install_opener()方法定义opener为全局opener
    urllib2.install_opener(opener)

    # 6. 构建 Request对象
    request = urllib2.Request('http://kehu.ntalker.com/', headers=header)

    # 7. 定义opener为全局opener后，可直接使用urlopen()发送请求
    response = urllib2.urlopen(request)

    # 8. 打印响应内容
    print response.read()


HttpBasicAuthHandlerFunc()