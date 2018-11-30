# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from .settings import *
import pymongo
import pymysql

class CsdnPipeline(object):
    def process_item(self, item, spider):
        print("-"*20)
        print("item；",item)


class CsdnmongoPipeline(object):
    def __init__(self):
        host = MONGO_HOST
        port = MONGO_PORT
        dbName = MONGO_DBNAME
        className = MONGO_CLASSNAME
        conn = pymongo.MongoClient(host=host,port=port)
        db = conn[dbName]
        self.myset = db[className]


    def process_item(self,item,spider):
        csdnInfo = dict(item)
        self.myset.insert(csdnInfo)
        print("存入数据库成功")

class CsdnmysqlPipeline(object):
    def __init__(self):
        host = MYSQL_HOST
        user = MYSQL_USER
        pwd = MYSQL_PWD
        dbName = MYSQL_DBNAME
        self.className = MYSQL_CLASSNAME
        self.db = pymysql.connect(host=host,user=user,password=pwd,db=dbName,charset='utf8')
        self.cursor = self.db.cursor()



    def process_item(self,item,spider):
        ins = 'insert into {} values (%s,%s,%s)'.format(self.className)
        L = [item['title'],item['time'],item['number']]
        self.cursor.execute(ins,L)
        self.db.commit()
        print("数据存入MySQL成功。。。")


