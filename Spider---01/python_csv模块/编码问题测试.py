# !/usr/bin/env/python
# _*_coding:utf-8 _*_
# author:LiangJianfei

import requests

user_agent = "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)"
headers = {"User-Agent":user_agent}
r = requests.get("http://seputu.com/",headers=headers)
# r.encoding = "utf-8"
r.encoding = r.apparent_encoding
print(r.text)