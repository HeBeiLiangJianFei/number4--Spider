# !/usr/bin/env/python
# _*_coding:utf-8 _*_
# author:LiangJianfei
from bs4 import BeautifulSoup

html_str = '''

<head>
    <title>Title</title>
</head>
<body>
    <p class="title"><b>the dormouse`s story</b></p>
    <p class="title"><b>the dormouse`s story</b></p>
    <p class="title"><b>the dormouse`s story</b></p>
    <p class="title"><b>the dormouse`s story</b></p>
    <p class="title"><b>the dormouse`s story</b></p>
</body>
</html>
'''

# soup = BeautifulSoup(html_str,"lxml",from_encoding="utf-8")
# print(soup.prettify())

# 第二种获取方法：
# 指定解析器
soup = BeautifulSoup(open("index.html"),features="lxml")
# print(soup.prettify())
ps = soup.select("body > p.title")
print(ps[0].select("a")[0].string)
# print(ps[0].attrs["href"])
# print(ps[0].get_text())
# print(ps[0].string)
