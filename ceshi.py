# !/usr/bin/env/python
# _*_coding:utf-8 _*_
# author:LiangJianfei
import json
import random

# for i in range(5):
#     print(random.randrange(1, 5))

# https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv14&productId=5973667&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1

# for page in range(1,200,2):
# #     url = "https://search.jd.com/Search?keyword=%E8%83%B8%E7%BD%A9&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E8%83%B8%E7%BD%A9&psort=3&page={}&s=123&click=0".format(page)
# #     print(url)
# #
# # '''
# # 第一步：获取所有页面的url
# # 第二步：获取页面中所有的bra连接
# # 第三步：解析每个bra的评价，购买时间、产品颜色、产品size、评论内容
# #
# #
# #
# #
# # '''
import re

import requests

# url = "https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv21&productId=8283244&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1"
id = "5973667"
# for i in range(10):
#     data = {
#         "callback":"fetchJSON_comment98vv14",
#         "productId":id,
#         "score": "0",
#         "sortType": "5",
#         "page": i,
#         "pageSize": "10",
#         "isShadowSku": "0",
#         "fold": "1"
#     }
url = "https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv14&productId=5973667&score=0&sortType=5&page=6&pageSize=10&isShadowSku=0&fold=1"
#
headers = {"UserAgent":"Mozilla/5.0"}

response = requests.get(url,headers = headers)
print("------>",response.url)
# url = response.url
# pat = re.compile(r'https:.*?&page=(.*?).*?fold=1')
# new_url = pat.findall(url,re.S)
# # print(url)
# print(new_url)


# print(response.text)
# response = response.text
# response = response.replace('fetchJSON_comment98vv14(', '')
# response = response.replace(')','')
# response = response.replace(';','')

# item = BraItem()
response = response.text
response = response.replace('fetchJSON_comment98vv14(', '')
response = response.replace(')', '')
response = response.replace(';', '')
jdDict = json.loads(response)
comments = jdDict['comments']
maxPage = jdDict['maxPage']
productComment = jdDict['productCommentSummary']
productid = productComment['productId']


# print(response)
jdDict = json.loads(response)
print("jdDict",jdDict['maxPage'])
print("productComment-->",productComment)
print("productid-->",productid)



