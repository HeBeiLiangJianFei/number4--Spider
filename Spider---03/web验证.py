# !/usr/bin/env/python
# _*_coding:utf-8 _*_
# author:LiangJianfei

'''web验证

auth = ("用户名","密码")
auth = ("tarenacode","code_2013")
'''

'''09-web验证'''

import requests
import re
from lxml import etree

class NoteSpider(object):
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
        self.url = "http://code.tarena.com.cn/"
        # self.proxies = {"http":"http://309435365:szayclhp@123.206.119.108:16817"}
        self.auth = ("tarenacode","code_2013")

    def getParsePage(self):
        try:
            # res = requests.get(self.url,proxies = self.proxies,headers = self.headers,auth = self.auth,timeout = 3)
            res = requests.get(self.url,headers = self.headers,auth = self.auth,timeout = 3)
            res.encoding = res.apparent_encoding
            html = res.text
        except Exception as e:
            print("获取HTML时出错：",e)
        else:
            text = etree.HTML(html)
            r_list2 = text.xpath('.//pre/a/text()')
            r_url = text.xpath('.//pre/a/@href')
            # pattern = re.compile('<pre>.*?<a href=".*?">(.*?)</a>',re.S)
            # r_list = pattern.findall(html)
            self.writePage(r_list2,r_url)


    def writePage(self,r_list,r_url):
        print("开始写入文件")
        with open("达内科技笔记.txt","a",encoding="utf-8") as f:
            for r_str,r_u in zip(r_list,r_url):
                f.write(r_str+":"+r_u+"\r\n")
        print("文件写入成功")



if __name__ =="__main__":
    spider = NoteSpider()
    spider.getParsePage()