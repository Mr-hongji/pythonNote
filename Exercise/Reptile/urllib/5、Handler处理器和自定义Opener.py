# -*- coding:utf-8 -*-
'''

    opener 是 urllib2.OpenerDirector 的实例，前面一直使用 urlopen ，
   它是一个特殊的 opener（也就是模块帮我们构建好的）

   基本的 urlopen() 方法不支持代理、cookie等其他的HTTP/HTTPS高级功能。所以支持这些功能：

    1、使用相关的 Handler 处理器来创建特定功能的处理器对象；
    2、然后通过urllib2.build_opener() 方法使用这些处理器对象，创建自定义 opener 对象；
    3、使用自定义的 opener 对象，调用 open() 方式发送请求


    HTTPHandler：支持处理 http 请求
    HTTPSHandler：支持处理 https 请求
    ProxyHandler: 代理Handler

'''

'''

HttpHandler & HttpsHandler

'''

import urllib2

def httpHandlerFunc():

    # HTTPHandler 中可以增加参数 debuglevel ，等于1 则会自动打开 debug模式
    # 程序执行时会打印收发包的信息 作为调试用
    httphandler = urllib2.HTTPHandler(debuglevel=1)

    opener = urllib2.build_opener(httphandler)

    # Request('http://www.baidu.com') url这么写会报错， 在最后一定要加上 ‘/ ’，用来表示根目录
    request = urllib2.Request('http://www.baidu.com/')

    response = opener.open(request)

    print(response.read())


'''

注意：

    Traceback (most recent call last):
  File "E:/PythonSpace/Exercise/����/urllib/5��Handler���������Զ���Opener.py", line 34, in <module>
    response = opener.open(request)
  File "D:\ProgramFiles\Python\lib\urllib2.py", line 437, in open
    response = meth(req, response)
  File "D:\ProgramFiles\Python\lib\urllib2.py", line 550, in http_response
    'http', request, response, code, msg, hdrs)
  File "D:\ProgramFiles\Python\lib\urllib2.py", line 475, in error
    return self._call_chain(*args)
  File "D:\ProgramFiles\Python\lib\urllib2.py", line 409, in _call_chain
    result = func(*args)
  File "D:\ProgramFiles\Python\lib\urllib2.py", line 558, in http_error_default
    raise HTTPError(req.get_full_url(), code, msg, hdrs, fp)
urllib2.HTTPError: HTTP Error 400: Bad Request


导致以上错误的原因是： 

   Request('http://www.baidu.com') 中的 url 后没有 '/ '

修改为：
    
    Request('http://www.baidu.com/') 即可
    
'''


def httpsHandlerFunc():

    httpshandler = urllib2.HTTPSHandler()

    opener = urllib2.build_opener(httpshandler)

    # Request('http://www.baidu.com') url这么写会报错， 在最后一定要加上 ‘/ ’，用来表示根目录
    request = urllib2.Request('https://www.baidu.com/')

    response = opener.open(request)

    print(response.read())


httpsHandlerFunc()