'''10_SSL证书认证示例.py'''
import requests

url = "https://www.12306.cn/mormhweb/"
headers = {"User-Agent":"Mozilla/5.0"}

res = requests.get(url,headers=headers,verify=False)
res.encoding = "utf-8"
print(res.text)
















