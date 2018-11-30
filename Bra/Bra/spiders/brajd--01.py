# !/usr/bin/env/python
# _*_coding:utf-8 _*_
# author:LiangJianfei


import json
import time
from ..items import *



class BrajdSpider(scrapy.Spider):
    name = 'brajd01'
    allowed_domains = ['jd.com']
    start_urls = ["https://search.jd.com/Search?keyword=%E8%83%B8%E7%BD%A9&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E8%83%B8%E7%BD%A9&psort=3&page=0&s=123&click=0"]
    def parse(self, response):
        productIdList = response.xpath('//ul[@class="gl-warp clearfix"]/li/@data-sku').extract()
        for id in productIdList:
            for page in (0,300):
                data = {
                    "callback": "fetchJSON_comment98vv14",
                    "productId": str(id),
                    "score": "0",
                    "sortType": "5",
                    "page": str(page),
                    "pageSize": "10",
                    "isShadowSku": "0",
                    "fold": "1"
                }
                print("data-----data--->",data)
                url = "https://sclub.jd.com/comment/productPageComments.action?"
                yield scrapy.FormRequest(url=url,method='GET',formdata=data,callback=self.getComments)



    def getComments(self,response):
        item = BraItem()
        response = response.text
        response = response.replace('fetchJSON_comment98vv14(', '')
        response = response.replace(')','')
        response = response.replace(';','')
        try:
            jdDict = json.loads(response)

            comments = jdDict['comments']
        # maxPage = jdDict['maxPage']
        # productComment = jdDict['productCommentSummary']
        # productid = productComment['productId']
            if comments:
                n = 0
                while n < len(comments):
                    comment = comments[n]
                    print("----"*30)
                    # item['productId'] = productid
                    item["content"] = comment['content']
                    item["productColor"] = comment['productColor']
                    item["creationTime"] = comment['creationTime']
                    item["productSize"] = comment['productSize']
                    n += 1
                    yield item
            else:
                pass
        except:
            pass
        # for page in range(1,int(maxPage)):
        #     data = {
        #         "callback": "fetchJSON_comment98vv14",
        #         "productId": str(productid),
        #         "score": "0",
        #         "sortType": "5",
        #         "page": str(page),
        #         "pageSize": "10",
        #         "isShadowSku": "0",
        #         "fold": "1"
        #     }
        #     print("data-----data--->", data)
        #     url = "https://sclub.jd.com/comment/productPageComments.action?"
        #     yield scrapy.FormRequest(url=url, method='GET', formdata=data, callback=self.getComments, dont_filter=True)



