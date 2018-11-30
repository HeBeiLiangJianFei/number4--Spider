'''12_ProxyHandler示例.py'''
import urllib.request

url = "http://www.baidu.com/"
proxy = {"http":"127.0.0.1:8888"}
# 创建Handler处理器对象
pro_hand = urllib.request.ProxyHandler(proxy)
# 创建自定义opener对象
opener = urllib.request.build_opener(pro_hand)
# opener对象open方法发请求
req = urllib.request.Request(url)
res = opener.open(req)
print(res.read().decode("utf-8"))














