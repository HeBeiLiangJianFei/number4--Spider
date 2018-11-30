# !/usr/bin/env/python
# _*_coding:utf-8 _*_
# author:LiangJianfei
import json
import time

import requests
for i in range(15):
    response = requests.get("http://127.0.0.1:5000/get")
    response.encoding = response.apparent_encoding
    HttpIp = response.text
    IP1 = HttpIp.split(":")[1:]
    str1 = ""
    for i in IP1:
        str1 += i
        str1 += ":"
    IP2 = str1.replace('}:','')
    print(IP2)
    time.sleep(2)