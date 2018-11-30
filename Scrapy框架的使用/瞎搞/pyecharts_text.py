# !/usr/bin/env/python
# _*_coding:utf-8 _*_
# author:LiangJianfei

from pyecharts import Bar
# from pyecharts.charts.bar import Bar

bar = Bar()
Bar("我的第一个图表", "这里是副标题")
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
bar.show_config()
bar.render()


import requests
url = "http"
req = requests.get(url)
req.encoding = req.apparent_encoding