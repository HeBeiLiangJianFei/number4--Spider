'''09_Web客户端验证.py'''
import requests
import re

class NoteSpider:
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla/5.0"}
        self.url = "http://code.tarena.com.cn/"
        self.proxies = {"http":"http://309435365:szayclhp@123.206.119.108:16817"}
        # auth参数存储用户名和密码(必须为元组)
        self.auth = ("tarenacode","code_2013")
    
    def getParsePage(self):
        res = requests.get(self.url,
                           proxies=self.proxies,
                           headers=self.headers,
                           auth=self.auth,
                           timeout=3)
        res.encoding = "utf-8"
        html = res.text
        print(html)
        p = re.compile('<a href=".*?>(.*?)</a>',re.S)
        r_list = p.findall(html)
        print(r_list)
        self.writePage(r_list)
        
    def writePage(self,r_list):
        print("开始写入文件...")
        with open("达内科技.txt","a") as f:
            for r_str in r_list:
                f.write(r_str + "\n\n")
        print("写入成功")
    
if __name__ == "__main__":
    spider = NoteSpider()
    spider.getParsePage()




















