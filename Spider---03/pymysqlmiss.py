# !/usr/bin/env/python
# _*_coding:utf-8 _*_
# author:LiangJianfei

'''pymyql回顾'''
'''创建一个Spiderdb,创建表t1'''

import  pymysql
import warnings

db = pymysql.connect("localhost","root","123456",charset="utf8")

cursor = db.cursor()

# 出现警告忽略
warnings.filterwarnings("ignore")

try:
    cursor.execute("create database if not exists spiderdb charset='utf8';")
    cursor.execute("use spiderdb;")
    cursor.execute("create table if not exists spidert1(id int);")
except  Warning:
    pass
ins = "insert into spidert1 values(%s)"
cursor.execute(ins,[1])
cursor.execute(ins,[2])
db.commit()
cursor.close()
db.close()

















