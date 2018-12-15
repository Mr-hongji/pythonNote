# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymongo, settings

class DoubanspiderPipeline(object):

    def __init__(self):

        # 从设置中获取参数
        host = settings.MONGO_HOST
        port = settings.MONGO_PORT
        db_name = settings.MONGO_DB_NAME
        collection_name = settings.MONGO_COLLECTION_NAME

        # 连接 MongoDB 数据库
        db_client = pymongo.MongoClient(host = host, port = port)
        db = db_client[db_name]
        self.coll = db[collection_name]

    def process_item(self, item, spider):

        self.coll.insert(item)
        return item
