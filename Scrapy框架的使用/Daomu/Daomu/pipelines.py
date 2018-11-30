# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

from .settings import *
import pymongo
class DaomuPipeline(object):
    def process_item(self, item, spider):
            print("--"*20)
            print("item:",item['bookChapter'])
            print("--"*20)


class DaomumongoPipeline(object):
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


class DaomumysqlPipeline(object):
    def __init__(self):
        host = MYSQL_HOST
        user = MYSQL_USER
        pwd = MYSQL_PWD
        dbName = MYSQL_DB
        self.className = MYSQL_CLASS
        self.db = pymysql.connect(host=host,user=user,password=pwd,db=dbName,charset='utf8')
        self.cursor = self.db.cursor()

    def process_item(self,item,spider):
        ins = 'insert into {} values (%s,%s,%s,%s,%s)'.format(self.className)
        L = [item['bookName'],item['bookTitle'],item['bookChapter'],item['chapterNum'],item['chapterHref']]
        self.cursor.execute(ins,L)
        self.db.commit()


