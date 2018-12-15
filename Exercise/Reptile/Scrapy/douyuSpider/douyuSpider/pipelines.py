# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline

import scrapy, os

from  scrapy.utils.project import get_project_settings

class DouyuspiderPipeline(ImagesPipeline):

    # 获取 settings 文件中的属性值
    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")

    def get_media_requests(self, item, info):
        image_url = item['image_url']

        yield scrapy.Request(image_url)


    # def item_completed(self, results, item, info):
    #
    #     path = results[0][1]['path']
    #
    #
    #     # 这个地方存在图片 和 nick_name 不符的问题
    #     os.rename(self.IMAGES_STORE + "/" + path, self.IMAGES_STORE + "/full/" + item['nick_name'] + '.jpg')
    #
    #     return item



