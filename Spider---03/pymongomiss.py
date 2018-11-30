# !/usr/bin/env/python
# _*_coding:utf-8 _*_
# author:LiangJianfei

'''pymongo回顾'''
'''pymongo 回顾'''

import pymongo

conn = pymongo.MongoClient("localhost",27017)
db = conn.spiderdb
myset = db.spidert1

myset.insert({"name":"Tom"})





