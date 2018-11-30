# !/usr/bin/env/python
# _*_coding:utf-8 _*_
# author:LiangJianfei
import pymongo

from lxml import etree

import requests

class LianJiaSpider(object):
    def __init__(self):
        self.baseurl = "https://tj.lianjia.com/zufang/bd1l1/"
        self.page = 1
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
        self.proxies = {}
        self.conn = pymongo.MongoClient("localhost",27017)
        self.db = self.conn.lian
        self.myset = self.db.housePrice
        print("数据库创建成功")

    def getPage(self,url):
        response = requests.get(url,headers = self.headers)
        response.encoding = response.apparent_encoding
        html = response.text
        print("获取页面成功")
        self.parsePage(html)

    def parsePage(self,html):
        text = etree.HTML(html)
        name_list = text.xpath('.//div[@class="where"]/a/span/text()')
        price_list = text.xpath('.//div[@class="price"]/span/text()')
        print("分析页面成功")
        self.writeToMongo(name_list,price_list)

    def writeToMongo(self,name_list,price_list):
        for name,price in zip(name_list,price_list):
            D = {"houseName":name.strip(),"totalPrice":price.strip()}
            self.myset.insert_one(D)
            print(D)

    def workOn(self):
        while 1:
            c = input("爬取属于y:")
            if c.lower() == "y":
                url = self.baseurl
                self.getPage(url)
                self.page += 1
            else:
                print("谢谢使用")
                break


if __name__ == "__main__":
    lianjia = LianJiaSpider()
    lianjia.workOn()



