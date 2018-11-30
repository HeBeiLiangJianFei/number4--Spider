import urllib.request
import urllib.parse

#拼接URL
baseurl = "http://www.baidu.com/s?wd="
key = input("请输入要搜索的内容:")
#进行quote()编码
key = urllib.parse.quote(key)

url = baseurl + key
print(url)
headers = {"User-Agent":"Mozilla/5.0"}
# 创建请求对象
req = urllib.request.Request(url,headers=headers)
# 获取响应对象
res = urllib.request.urlopen(req)
html = res.read().decode("utf-8")

#写入本地文件
with open("搜索2.html","w",encoding="gb18030") as f:
    f.write(html)