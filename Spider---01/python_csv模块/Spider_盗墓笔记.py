# !/usr/bin/env/python
# _*_coding:utf-8 _*_
# author:LiangJianfei
import csv
import re
from lxml import etree
import requests

user_agent = "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)"
headers = {"User-Agent":user_agent}
r = requests.get("http://seputu.com/",headers=headers)
# r.encoding = "utf-8"
r.encoding = r.apparent_encoding
html = etree.HTML(r.text)
div_mulus = html.xpath('.//*[@class="mulu"]')
pattern = re.compile(r'\s*\[(.*)\]\s+(.*)')
rows = []

for div_mulu in div_mulus:
    div_h2 = div_mulu.xpath("./div[@class='mulu-title']/center/h2/text()")
    if len(div_h2)>0:
        h2_title = div_h2[0]
        a_s = div_mulu.xpath('./div[@class="box"]/ul/li/a')
        for a in a_s:
            href = a.xpath("./@href")[0]
            box_title = a.xpath("./@title")[0]
            match = pattern.search(box_title)
            if match != None:
                date = match.group(1)
                real_title = match.group(2).encode("utf-8")
                content = (h2_title,real_title,href,date)
                print(content)
                rows.append(content)

headers = ["title","real_title","href","date"]

with open("盗墓笔记.csv","a",newline="",encoding="UTF-8") as f:
    f_csv = csv.writer(f,)
    f_csv.writerow(headers)
    f_csv.writerows(rows)