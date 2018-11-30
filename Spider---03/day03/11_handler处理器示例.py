'''Handler处理器示例.py'''
import urllib.request

url = "http://www.baidu.com/"
# 创建Handler处理器对象
http_handler = urllib.request.HTTPHandler()
#proxy_handler = urllib.request.ProxyHandler()
# 创建自定义的opener对象
opener = urllib.request.build_opener(http_handler)
# 利用opener对象的open()方法发请求
req = urllib.request.Request(url)
res = opener.open(req)
print(res.read().decode("utf-8"))









