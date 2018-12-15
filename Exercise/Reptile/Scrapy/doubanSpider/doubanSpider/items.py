# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanspiderItem(scrapy.Item):

    # 标题
    m_title = scrapy.Field()

    # 演员
    m_bd = scrapy.Field()

    # 评分
    m_rationgNum = scrapy.Field()

    # 简介
    m_quote = scrapy.Field()

    # 数据存入 MongoDB 的时候，程序会生成一个 ObjectId 赋值给 这个 _id 属性
    _id = scrapy.Field()
