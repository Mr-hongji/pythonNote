# -*- coding:utf-8 -*-
''''''
'''

Cookie

        * 是指某些网站服务器为了辨别用户身份和进行Session跟踪，而储存在用户浏览器上的文本文件.
    Cookie 可以保持登录信息到用户下次与服务器的会话。

之前用的都是使用抓包的方式，直接获取header中的 cookie 信息，然后放到程序中的 header 中



cookielib 库 和 HTTPCookieProcessor 处理器

    * 在 Python 中处理 Cookie，一般是通过 cookielib 模块和 urllib2 模块的 HTTPCookieProcessor 处理器类一起使用。


cookielib 模块
    
    * 主要作用是提供用于存储cookie的对象
    
    * 该模块主要的对象有:
        - CookieJar
            管理HTTP cookie值、存储HTTP请求生成的cookie、向传出的HTTP请求添加cookie的对象。
            整个cookie都存储在内存中，对CookieJar实例进行垃圾回收后cookie也将丢失。
            
        - FileCookieJar(filename,delayload=None,policy=None)
            从CookieJar派生而来，用来创建FileCookieJar实例，检索cookie信息并将cookie存储到文件中。
            filename是存储cookie的文件名。delayload为True时支持延迟访问访问文件，
            即只有在需要时才读取文件或在文件中存储数据。
        
        - MozillaCookieJar(filename,delayload=None,policy=None)
            从FileCookieJar派生而来，创建与Mozilla浏览器 cookies.txt兼容的FileCookieJar实例。
            
        - LWPCookieJar(filename,delayload=None,policy=None)
            从FileCookieJar派生而来，创建与libwww-perl标准的 Set-Cookie3 文件格式兼容的FileCookieJar实例。

    * 大多数情况下，我们只用CookieJar()，如果需要和本地文件交互，就用 MozillaCookjar() 或 LWPCookieJar()



HTTPCookieProcessor处理器
    
    * 主要作用是处理这些cookie对象，并构建handler对象。

'''

import urllib2, urllib
import cookielib

cookiejar = None


def printCookieStr():

    '''
    打印 cookiejar 中自动保存的 cookie 值
    :return:
    '''
    global cookiejar

    # 可以按标准格式将保存的Cookie打印出来
    cookieStr = ""
    for item in cookiejar:
        cookieStr = cookieStr + item.name + "=" + item.value + ";"

    ## 舍去最后一位的分号
    print cookieStr[:-1]

    cookiejar = None


def CookieJarTest():

    '''
    使用 cookielib 和 post 方式模拟登录人人网并获取登录后才能访问的页面信息
    :return:
    '''
    global cookiejar

    requestURL = 'http://www.renren.com/PLogin.do'

    header = {
        'User - Agent': 'Mozilla / 5.0(Windows NT 6.1;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 67.0.3396.99Safari / 537.36'
    }

    # 需要登录的账户和密码
    data = {
        'email':'lyjn5126@163.com',
        'password':'shihongji123'
    }

    data = urllib.urlencode(data)

    # 构建一个CookieJar对象实例来保存cookie
    cookiejar = cookielib.CookieJar()

    # 使用HTTPCookieProcessor()来创建cookie处理器对象，参数为CookieJar()对象
    cookie_handler = urllib2.HTTPCookieProcessor(cookiejar)

    # 通过 build_opener() 来构建opener
    # opener包含用户登录后的Cookie值，可以直接访问那些登录后才可以访问的页面
    opener = urllib2.build_opener(cookie_handler)

    # 设置全局的 opener
    urllib2.install_opener(opener)

    request = urllib2.Request(requestURL, data = data, headers = header)

    response = urllib2.urlopen(request)

    # 打印抓取到的页面信息
    print(response.read())

    # 赵洁琼  互联网前端工程师 的主页
    # 如果不使用 cookie ，直接登录主页的话，只能取到登录页面信息
    # 使用 cookie 就可以直接获取"赵洁琼" 主页信息
    response = urllib2.urlopen('http://www.renren.com/256450404/profile')
    print(response.read())





'''

MozillaCookieJar

'''

def saveCookieToFile():

    '''

     访问网站获得cookie，并把获得的cookie保存在cookie文件中

    :return:
    '''

    # 保存cookie的本地磁盘文件名
    filename = 'cookie.txt'
    requestURL = 'http://www.baidu.com/'

    # 声明一个MozillaCookieJar(有save实现)对象实例来保存cookie，之后写入文件
    cookie = cookielib.MozillaCookieJar(filename)

    http_handler = urllib2.HTTPCookieProcessor(cookie)

    opener = urllib2.build_opener(http_handler)

    urllib2.install_opener(opener)

    response = urllib2.urlopen(requestURL)
    print(response.read())

    # 保存cookie到本地文件
    cookie.save()




def loadCookieFile():

    '''

    从文件中获取cookies，做为请求的一部分去访问

    :return:
    '''

    # 保存cookie的本地磁盘文件名
    filename = 'cookie.txt'
    requestURL = 'http://www.baidu.com/'

    # 声明一个MozillaCookieJar(有save实现)对象实例来保存cookie，之后写入文件
    cookie = cookielib.MozillaCookieJar()

    # 从文件中读取cookie内容到变量
    cookie.load(filename)

    http_handler = urllib2.HTTPCookieProcessor(cookie)

    opener = urllib2.build_opener(http_handler)

    urllib2.install_opener(opener)

    response = urllib2.urlopen(requestURL)
    print(response.read())




# CookieJarTest()
# printCookieStr()

saveCookieToFile()
