# -*- coding:utf-8 -*-

'''

1、爬取 豆瓣电影排行前 250 的电影信息， 并保存到 MongoDB

2、通过使用下载中间件生成随机 agent 和 proxy,来访问豆瓣排行榜 url

'''

import scrapy
from ..items import DoubanspiderItem

class doubanSpider(scrapy.Spider):

    name = 'douban'

    allowed_domains = ['douban.com']

    url = 'https://movie.douban.com/top250?start='

    # 每次 增加 25
    offset = 0

    start_urls = [
        url + str(offset)
    ]


    def parse(self, response):

        m_list = response.xpath('//div[@class="info"]')

        for m in m_list:

            item = DoubanspiderItem()

            title = m.xpath('.//span[@class="title"][1]/text()')
            if len(title) > 0:
                item['m_title'] = title.extract()[0].strip()

            bd = m.xpath('.//div[@class="bd"]/p/text()')
            if len(bd) > 0:
                item['m_bd'] = bd.extract()[0].strip()

            rationgNum = m.xpath('.//div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()')
            if len(rationgNum) > 0:
                item['m_rationgNum'] = rationgNum.extract()[0].strip()

            quote = m.xpath('.//div[@class="bd"]/p[@class="quote"]/span/text()')
            if len(quote) > 0:
                item['m_quote'] = quote.extract()[0].strip()

            yield item


        if self.offset < 225:
            self.offset += 25
            yield scrapy.Request(self.url + str(self.offset), callback = self.parse)

