#coding:cp936


import scrapy
import json
from ..items import DouyuspiderItem

class douyuSpider(scrapy.Spider):

    name = 'douyu'
    allowed_domains = ['douyu.com']

    url = 'https://www.douyu.com/gapi/rkc/directory/0_0/'

    offset = 1

    start_urls = [url + str(offset)]

    def parse(self, response):
        results = json.loads(response.text)['data']['rl']

        item = DouyuspiderItem()

        for info in results:

            item['room_name'] = info['rn']
            item['nick_name'] = info['nn']
            item['category_name'] = info['c2name']
            item['image_url'] = info['rs1']

            print(item['room_name'] + ', ' +  item['nick_name'] + ', ' + item['image_url'])

            yield item


        if self.offset < 66:
            self.offset += 1


        yield scrapy.Request(self.url + str(self.offset), callback = self.parse)



