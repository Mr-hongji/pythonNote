# -*- coding:utf-8 -*-

'''

中文文档：

http://docs.python-requests.org/zh_CN/latest/user/quickstart.html



SSL证书问题：

    requests 在请求 https 的时候加入了 ssl证书验证，在访问 https 时 设置 verify=False 忽略SSL验证



'''


import requests


def get_post_req():
    '''

    Get \ Post 方式请求

    :return:
    '''
    url = 'https://www.zhihu.com/'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }

    # verify = False | True （否 | 是） 是否开启SSL验证
    # timeout = 10 请求超时时间（单位：秒）

    # get 方式
    response = requests.get(url,headers = headers, verify = False, timeout = 10)
    print(response.content)

    # post 方式
    response = requests.post(url, headers = headers, verify = False, timeout = 10)
    print(response.content)



def re_param():
    '''
    请求传参
    :return:
    '''

    payload = {'key1': 'value1', 'key2': ['value2', 'value3']}

    # Get 方式
    r = requests.get('http://httpbin.org/get', params = payload)
    print(r.url) # http://httpbin.org/get?key2=value2&key2=value3&key1=value1


    # Post 方式一
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.post("http://httpbin.org/post", data = payload)
    print(r.text)

    '''
    
        "form": {
            "key1": "value1", 
            "key2": "value2"
        }
    
    '''


    # Post 方式二
    payload = (('key1', 'value1'), ('key1', 'value2'))
    r = requests.post('http://httpbin.org/post', data = payload)
    print(r.text)

    '''
        "form": {
            "key1": [
              "value1", 
              "value2"
            ]
        }

    '''

re_param()

