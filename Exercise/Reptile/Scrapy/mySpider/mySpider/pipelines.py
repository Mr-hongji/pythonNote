# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# 管道（英语：Pipeline）

import json

class tencentSpiderPipeline(object):

    def __init__(self):
        self.f = open('tencent.json', 'w')

    def process_item(self, item, spider):

        # dict(item) 把item对象 转成 字典形式
        self.f.write(json.dumps(dict(item), ensure_ascii=False).encode('utf-8') + '\n')

        # 必须return item 对象， return之后 这个 item 就不会再被 pipeline 做处理了，否则下一次pipeline处理的还是这个 item 对象
        return item

    def close_spider(self, spider):
        self.f.close()
