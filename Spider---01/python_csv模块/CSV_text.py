# !/usr/bin/env/python
# _*_coding:utf-8 _*_
# author:LiangJianfei

''''''
import time

'''CSV其文件是以纯文本的形式存储表格数据（数字和文本）。纯文本
意味着该文件是一个字符串序列，不含必须向二进制数一样被解读的数据

每条记录由字段组成，字段间的分隔符是其他字符串或字符串，最常见的是逗号或制表符。
通常，所有记录都是完全相同的字段序列。

'''
'''python使用csv库来读写CSV文件。要将上面CSV文件的示例内容写成qiye.csv文件，
   需要用到Writer对象   
'''

# import csv
#
# headers = {"ID","UserName","Password","Age","country"}
# rows = {
#     (1001,"qiye","qiye_pass",24,"China"),
#     (1002,"Mary","Mary_pass",20,"USA"),
#     (1003,"Jack","Jack_pass",20,"USA"),
# }
#
#
# with open("qiye.csv","a", newline="", encoding="UTF-8") as f:
#     f_csv = csv.writer(f)
#     f_csv.writerow(headers)
#     f_csv.writerows(rows)


'''讲解从csv文件中读取内容 这种方式返回的内容是以列表形式返回'''
# import csv
#
# with open("qiye.csv") as f:
#     f_csv = csv.reader(f)
#     headers = next(f_csv)
#     print(headers)
#     for row in f_csv:
#         print(row)

'''讲解从csv文件中读取内容 这种方式返回的内容是元组形式返回'''
# from collections import namedtuple
# import csv
# with open("qiye.csv") as f:
#     f_csv = csv.reader(f)
#     headings = next(f_csv)
#     Row = namedtuple("Row",headings)
#     for r in f_csv:
#         row = Row(*r)
#         print(row.UserName,row.Password)
#         print(row)


# from selenium import webdriver
# b = webdriver.Chrome()
# b.get("http://www.baidu.com")
# time.sleep(10)
# b.close()
