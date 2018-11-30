import urllib.request
import urllib.parse
import random
import time

# 随机获取1个User-Agent
header_list = [{"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"},
               {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"},
               {"User-Agent":"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB7.0)"}]
headers = random.choice(header_list)
# 主体程序
name = input("请输入贴吧名:")
begin = int(input("请输入起始页:")) 
end = int(input("请输入终止页:"))
# 对贴吧名name进行编码
kw = {"kw":name}
kw = urllib.parse.urlencode(kw)
# 拼接URL,发请求,获响应
for i in range(begin,end+1):
    # 拼接URL
    pn = (i-1)*50
    baseurl = "http://tieba.baidu.com/f?"
    url = baseurl + kw + "&pn=" + str(pn)
    # 发起请求
    req = urllib.request.Request(url,headers=headers)
    res = urllib.request.urlopen(req,timeout=5)
    time.sleep(2)
    html = res.read().decode("utf-8")
    # 写入文件
    filename = "第" + str(i) + "页.html"
    with open(filename,"w",encoding="utf-8") as f:
        print("正在爬取第%d页" % i)
        f.write(html)
        print("第%d页爬取成功" % i)
        print("*" * 30)












