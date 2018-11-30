'''01_普通代理示例.py'''
import requests

url = "http://www.baidu.com/"
proxies = {"http":"http://183.129.207.82:11597"}
headers = {"User-Agent":"Mozilla/5.0"}

res = requests.get(url,proxies=proxies,headers=headers)
print(res.status_code)



















