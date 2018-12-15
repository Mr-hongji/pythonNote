# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuspiderItem(scrapy.Item):

    # 房间名
    room_name = scrapy.Field()

    # 主播名
    nick_name = scrapy.Field()

    # 类别名称
    category_name = scrapy.Field()

    # 图片url
    image_url = scrapy.Field()

    images = scrapy.Field()


