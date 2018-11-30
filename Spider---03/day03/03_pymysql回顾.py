'''创建一个库spiderdb,创建表t1,插入1条记录'''
import pymysql
import warnings

# 创建数据库连接对象
db = pymysql.connect("localhost","root",
                     "123456",charset="utf8")
# 创建游标对象
cursor = db.cursor()
# 执行语句
# 过滤警告
warnings.filterwarnings("ignore")
try:
    cursor.execute("create database if not exists spiderdb")
    cursor.execute("use spiderdb")
    cursor.execute("create table if not exists t1(id int)")
except Warning:
    pass

ins = "insert into t1 values(%s)"
cursor.execute(ins,[1])
cursor.execute(ins,[2])
# 提交
db.commit()
# 关闭
cursor.close()
db.close()





