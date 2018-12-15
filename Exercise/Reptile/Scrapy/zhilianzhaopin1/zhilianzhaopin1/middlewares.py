# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


import random, base64, settings

class zhilianProxyMiddleWares(object):

    proxys = settings.PROXYS


    def process_request(self, request, spider):

        if len(self.proxys) <= 0:
            return

        proxy = random.choice(self.proxys)

        request.meta['proxy'] = 'http://' + proxy['ip_port']
        if proxy['uname_pwd'] != '':
            request.headers['Proxy-Authorization'] = 'Basic ' + base64.b64encode(proxy['uname_pwd'])

        return None


