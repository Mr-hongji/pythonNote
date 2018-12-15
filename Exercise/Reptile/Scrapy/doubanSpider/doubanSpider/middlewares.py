# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

import settings, random, base64


'''

    中间件类：
        
        程序在发送请求之前会先经过中间件，在中间件中修改访问的参数设置（如：请求的 Agent   和  代理），
        设置完成后，程序才会吧请求发送出去

'''

class doubanSpiderAgentsMiddleWares(object):

    '''
        agent 下载中间件

        随机生成访问的 agent

    '''

    def __init__(self):

        # 读取 settings 文件中的 agent 集合
        self.agents = settings.AGENTS

    def process_request(self, request, spider):

        # 每次请求都从集合中随机获取一个agent
        agent = random.choice(self.agents)

        print(agent)
        request.headers.setdefault(b'User-Agent', agent)

        return None



class doubanSpiderProxyMiddleWares(object):

    '''

        使用随机代理

    '''
    def __init__(self):

        # 读取 settings 文件中的 代理集合
        self.proxys = settings.PROXYS

    def process_request(self, request, spider):

        # 每次请求都随机获取一个 代理
        proxy = random.choice(self.proxys)
        print(proxy)

        request.meta['proxy'] = 'http://' + proxy['host_port']

        # 如果代理是私人代理 则 设置 用户名和密码
        if proxy['user_pwd'] != '':

            # 代理 的用户名和密码 使用 base64 编码（原因： 防止用户名和密码过长）
            user_pwd = base64.b64encode(proxy['user_pwd'])

            request.headers['Proxy-Authorization'] = 'Basic ' + user_pwd

        return None