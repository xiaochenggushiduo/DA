# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#在setting已经打开item

from pymongo import MongoClient

client = MongoClient()#本机不用写
collection = client["tencent"]["hr"]

class TencentPipeline(object):
    def process_item(self, item, spider):
        print(item)
        collection.insert(item)
        return item
