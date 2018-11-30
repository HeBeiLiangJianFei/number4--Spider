# !/usr/bin/env/python
# _*_coding:utf-8 _*_
# author:LiangJianfei
import os
import urllib.request
import requests
from lxml import etree

def Schedule(blocknum,blocksize,totalsize):
    ''''''
    '''
    blocknum:意见下载的数据块
    blocksize:数据块的大小
    totalsize：远程文件的大小
    '''
    per = 100.0*blocknum*blocksize/totalsize
    if per >100:
        per = 100
    print("当前下载进度：{}".format(per))


user_agent = "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)"
headers = {"User-Agent":user_agent}

r = requests.get("http://www.ivsky.com/tupian/jiaju/",headers=headers)
r.encoding = r.apparent_encoding
html = etree.HTML(r.text)

img_urls = html.xpath("//img/@src")
i = 0
path = os.path.dirname(__file__)
path2 = os.path.join(path,"photo/")
for img_url in img_urls:
    print(img_url)
    urllib.request.urlretrieve(img_url,path2+"img"+str(i)+".jpg",Schedule)
    i+=1


