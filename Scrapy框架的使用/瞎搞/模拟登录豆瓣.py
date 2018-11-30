# !/usr/bin/env/python
# _*_coding:utf-8 _*_
# author:LiangJianfei
import pytesseract
import  requests
from lxml import etree
from PIL import Image
import urllib.request
# url = "https://accounts.douban.com/login"
# headers = {"User-Agent":"Mozilla/5.0"}

# rep = requests.get(url,headers)
# rep.encoding = rep.apparent_encoding
# html = rep.text
#
#
#
#
# # 使用lxml获取验证码图片链接
# result = etree.HTML(html)
# s = result.xpath('//*[@id="captcha_image"]/@src')[0]
# urllib.request.urlretrieve(s,"D:\Scrapy框架的使用\瞎搞\y.jpg")
image = Image.open("y.jpg")
print(image)
s = pytesseract.image_to_string(image)
print(s)


# 访问验证码图片链接，到得HTML（字节流）


# 把图片保存到本地



# 把这个字符串输入到验证码框中



