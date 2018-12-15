# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import json
from datetime import datetime

class ZhilianzhaopinPipeline(object):

    def __init__(self):
        self.f = open('job.json', 'w')

    def process_item(self, item, spider):
        # self.f.write(json.dumps(dict(item), ensure_ascii=False).encode('utf-8') + '\n')
        item["crawled"] = datetime.utcnow()
        item["spider"] = spider.name
        return item

    def close_spider(self, spider):
        self.f.close()
