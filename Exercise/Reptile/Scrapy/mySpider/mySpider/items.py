# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

# 这个 items 其实就相当于 java 中的对象实体类 （vo 类）

import scrapy


class itcastSpiderItem(scrapy.Item):

    # 教师名称
    name = scrapy.Field()

    # 教师职称
    title= scrapy.Field()

    # 教师简介
    synopsis = scrapy.Field()


class tencentSpiderItem(scrapy.Item):

    # 职位名称
    position_name = scrapy.Field()

    # 职位类别
    position_category = scrapy.Field()

    # 人数
    number = scrapy.Field()

    # 地点
    locale = scrapy.Field()

    # 发布时间
    release_time = scrapy.Field()