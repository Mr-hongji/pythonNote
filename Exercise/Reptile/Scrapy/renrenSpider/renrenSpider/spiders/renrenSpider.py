# -*- coding:utf-8 -*-
'''

    Scrapy 模拟人人网登录

    这个是Scrapy 模拟登录的正常写法
'''

import scrapy

class renrenSpider(scrapy.Spider):

    name = 'renren'

    allowed_domains = ['renren.com']

    start_urls = [
        'http://www.renren.com/256450404/profile',
        'http://www.renren.com/250987359/profile',
        'http://www.renren.com/435297442/profile'
    ]

    pageName = 0

    # 重写 start_requests 方法
    # 重写该方法之后，程序启动时，就不会自动访问 start_urls 中的url
    def start_requests(self):

        url =  'http://www.renren.com/PLogin.do'

        # Post 请求使用 FormRequest() 方法，传参 formdata
        yield scrapy.FormRequest(url = url, formdata = {'email':'lyjn5126@163.com', 'password':'shihongji123'}, callback = self.parse)

    def parse(self, response):

        # 登录成功后开始循环访问关注的好友页面
        for url in self.start_urls:
            yield scrapy.Request(url = url, callback = self.parse_page)


    def parse_page(self, response):
        global pageName
        self.pageName += 1
        with open(str(self.pageName) + '.html', 'w') as f:
            f.write(response.body)