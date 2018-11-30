'''10_有道翻译post.py'''
import requests
import json

# 请输入你要翻译的内容
key = input("请输入要翻译的内容:")
# post方法要求data为字典格式
data = {"i": key,
        "from":"AUTO",
        "to":"AUTO",
        "smartresult":"dict",
        "client":"fanyideskweb",
        "salt":"1540373170893",
        "sign":"a5d9b838efd03c9b383dc1dccb742038",
        "doctype":"json",
        "version":"2.1",
        "keyfrom":"fanyi.web",
        "action":"FY_BY_REALTIME",
        "typoResult":"false"
    }

# 发请求,获取响应
# url为POST的地址,抓包工具抓到的,此处去掉 _o
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
headers = {"User-Agent":"Mozilla/5.0"}
# 此处data为form表单数据
res = requests.post(url,data=data,headers=headers)
res.encoding = "utf-8"
html = res.text
# 把json格式字符串转换为Python中字典
r_dict = json.loads(html)
result = r_dict['translateResult'][0][0]["tgt"]
print(result)

# 作业 ：把翻译后的结果输出来
# 请输入要翻译的内容 ：你好
# hello

#{'type': 'ZH_CN2EN', 
# 'errorCode': 0, 
# 'elapsedTime': 7, 
# 'translateResult': 
# [[{'src': '风云', 'tgt': 'Occasion'}]]
#}











