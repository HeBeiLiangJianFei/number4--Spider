'''08_requests模块示例.py'''
import requests

url = "http://www.baidu.com/"
headers = {"User-Agent":"Mozilla/5.0"}
# 发请求获响应
response = requests.get(url,headers=headers)
response.encoding = "utf-8"
# 获取字符串
print(type(response.text))
# 获取字节流
print(type(response.content))
# 返回服务器响应码
print(response.status_code)
# 返回数据的URL
print(respone.url)









#print(respone.encoding)
# 默认返回编码格式 ：ISO-8859-1








