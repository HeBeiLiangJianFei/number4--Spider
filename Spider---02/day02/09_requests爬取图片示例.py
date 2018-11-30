import requests

url = "http://dingyue.nosdn.127.net/LftiDijLShX6y8NWnEI606fo0TJmFMRIByj4HniV9GypR1539753512019.jpg"
headers = {"User-Agent":"Mozilla/5.0"}

res = requests.get(url,headers=headers)
html = res.content

with open("颖宝.jpg","wb") as f:
    f.write(html)

print("图片下载成功")












