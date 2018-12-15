# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DongguanspiderItem(scrapy.Item):

    # 问题标题
    q_title = scrapy.Field()

    # 问题编号
    q_number = scrapy.Field()

    # 问题内容
    q_content = scrapy.Field()

    # 问题解决状态
    q_state = scrapy.Field()

    # 提问时间
    q_time = scrapy.Field()

    # 提问者昵称
    q_nickname = scrapy.Field()

    # url
    q_url = scrapy.Field()

