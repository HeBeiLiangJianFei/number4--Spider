import urllib.request

url = "http://www.baidu.com/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
# 1.创建请求对象(有User-Agent)
req = urllib.request.Request(url,headers=headers)
# 2.获取响应对象(urlopen())
res = urllib.request.urlopen(req)
# 3.响应对象read().decode("utf-8")
#html = res.read().decode("utf-8")
#print(html)
print(res.getcode())
print(res.geturl())












