import urllib.request

# response为响应对象
response = urllib.request.urlopen("http://www.baidu.com/")
html = response.read().decode("utf-8")

print(html)


#encode()  字符串 --> bytes数据类型
#decode()  bytes数据类型 --> 字符串






