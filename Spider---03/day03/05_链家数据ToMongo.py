'''05_链家数据ToMongo.py'''
import requests
import re
import pymongo

class LianjiaSpider:
    def __init__(self):
        self.baseurl = 
        self.page = 1
        self.headers = {"User-Agent":"Mozilla/5.0"}
        self.proxies = {}
        self.conn = pymongo.MongoClient("localhost",27017)
        self.db = self.conn.Lianjia
        self.myset = self.db.housePrice

    def getPage(self,url):
        res = requests.get(url,proxies=self.proxies,headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        self.parsePage(html)

    def parsePage(self,html):
        p = re.compile('<div class="houseInfo".*?data-el="region">(.*?)</a>.*?<div="totalPrice">.*?<span>(.*?)</span>(.*?)</div>',re.S)
        r_list = p.findall(html)
        # [("天通苑","480","万"),()..]
        self.writeTomongo(r_list)

    def writeTomongo(self,r_list):
        for r_tuple in r_list:
            D = {"houseName":r_tuple[0].strip(),\
        "totalPrice":float(r_tuple[1].strip())*10000}
            self.myset.insert(D)

    def workOn(self):
        pass

if __name__ == "__main__":
    spider = LianjiaSpider()
    spider.workOn()
