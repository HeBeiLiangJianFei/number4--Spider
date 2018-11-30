'''09_requests.get.params.py'''
import requests

headers = {"User-Agent":"Mozilla/5.0"}
url = "http://www.baidu.com/s?"
key = input("请输入要搜索的内容:")
params = {"wd":key}

# 自动编码,自动拼接URL,params必须为字典
res = requests.get(url,params=params,headers=headers)
# 指定utf-8
res.encoding = "utf-8"
print(res.text)




















