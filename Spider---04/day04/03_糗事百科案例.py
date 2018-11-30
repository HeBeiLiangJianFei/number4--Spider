'''03_糗事百科案例.py'''
import requests
from lxml import etree
import pymongo

class QiuShiSpider:
    def __init__(self):
        self.url = "https://www.qiushibaike.com/8hr/page/1/"
        self.headers = {"User-Agent":"Mozilla/5.0"}
        self.conn = pymongo.MongoClient("localhost",27017)
        self.db = self.conn.Baikedb
        self.myset = self.db.baikeset
        
    def getPage(self):
        res = requests.get(self.url,headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        self.parsePage(html)
    
    def parsePage(self,html):
        parseHtml = etree.HTML(html)
        # 基准xpath,每个段子的列表
        base_list = parseHtml.xpath('//div[contains(@id,"qiushi_tag_")]')
        # 遍历每个段子的节点对象(base)
        for base in base_list:
            # 用户昵称
            username = base.xpath('./div/a/h2')
            if len(username) == 0:
                username = "匿名用户"
            else:
                username = username[0].text
            # 段子内容
            content = base.xpath('.//div[@class="content"]/span')[0].text
            # 好笑数量
            # [<element.好笑数量>,<eleme.评论>,<element...>]
            laughNum = base.xpath('.//i')[0].text 
            # 评论数量
            pingNum = base.xpath('.//i')[1].text
            
            d = {
                  "username":username.strip(),
                  "content":content.strip(),
                  "laughNum":laughNum.strip(),
                  "pingNum":pingNum.strip()
              }
            self.myset.insert(d)
            print("存入数据库成功")

if __name__ == "__main__":
    spider = QiuShiSpider()
    spider.getPage()
    
    
    
    
    
    
    























