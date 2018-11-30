'''02_私密代理示例.py'''
import requests

url = "http://httpbin.org/get"
headers = {"User-Agent":"Mozilla/5.0"}
proxies = {"http":"http://309435365:szayclhp@123.206.119.108:16817"}

res = requests.get(url,proxies=proxies,headers=headers)
res.encoding = "utf-8"
print(res.text)









