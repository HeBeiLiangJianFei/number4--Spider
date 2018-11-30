# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from .settings import *
import pymongo



class BraPipeline(object):
    def process_item(self, item, spider):
        # url_list = []
        # url_list.append(item['url'])

        return item


class JdBramongoPipeline(object):
    def __init__(self):
        host = MONGODB_HOST
        port = MONGODB_PORT
        dbName = MONGODB_DBNAME
        docName = MONGODB_DOCNAME
        conn = pymongo.MongoClient(host=host,port=port)
        db = conn[dbName]
        self.myset = db[docName]


    def process_item(self,item,spider):
        # 将item对象转为字典
        bookInfo = dict(item)
        self.myset.insert(bookInfo)
        print("存入数据库成功")
        return item
