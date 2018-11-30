# !/usr/bin/env/python
# _*_coding:utf-8 _*_
# author:LiangJianfei


from bs4 import BeautifulSoup
import requests
from lxml import etree

url = "https://www.qiushibaike.com"
headers = {"User-Agent":"Mozilla/5.0"}
html = ""
try:
    rep = requests.get(url,headers = headers)
    rep.encoding = rep.apparent_encoding
    html = rep.text
except Exception as e:
    print("获去网页失败：",e)

soup = BeautifulSoup(html,"lxml")
# r_list = soup.find_all("div",attrs={"class":"content"})
r_list = soup.select('#qiushi_tag_121176852 > a.contentHerf > div')

# result = etree.HTML(html)
# r_list = result.xpath('//*[@id="content-left"]//div/span[1]')

for r in r_list:
    print(r.span.get_text())




