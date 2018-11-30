# -*- coding: utf-8 -*-
import json
import re
import scrapy
from urllib3 import PoolManager
http = PoolManager()

from ..items import *


class BrajdSpider(scrapy.Spider):
    name = 'brajd'
    allowed_domains = ['https://search.jd.com']
    start_urls = ["https://search.jd.com/Search?keyword=%E8%83%B8%E7%BD%A9&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E8%83%B8%E7%BD%A9&psort=3&page=0&s=123&click=0"]
    # for i in range(1,200,2):
    #     url = "https://search.jd.com/Search?keyword=%E8%83%B8%E7%BD%A9&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E8%83%B8%E7%BD%A9&psort=3&page={}&s=123&click=0".format(i)
    #     start_urls.append(url)


    def parse(self, response):
        item = BraItem()
        # 获取所有商品url所需IP
        productIdList = response.xpath('//ul[@class="gl-warp clearfix"]/li/@data-sku').extract()
        for ip in productIdList:
            self.getMaxPage(ip)
            # jdDict,maxPage = self.getInfo()
            num = 0
            while num <= self.getMaxPage(ip):
                try:
                    jdDict = self.getComments(ip, num)
                    comments = jdDict['comments']
                    n = 0
                    while n < len(comments):
                        comment = comments[n]
                        item['content'] = comment['content'].encode(encoding='ISO-8859-1').decode('GB18030')
                        item['productColor'] = comment['productColor'].encode(encoding='ISO-8859-1').decode('GB18030')
                        item['creationTime'] = comment['creationTime'].encode(encoding='ISO-8859-1').decode('GB18030')
                        item['productSize'] = comment['productSize'].encode(encoding='ISO-8859-1').decode('GB18030')
                        yield item
                        n += 1
                    num += 1
                except Exception as e:
                    print(e)
                    continue
        for i in range(1,200,2):
            next_url = "https://search.jd.com/Search?keyword=%E8%83%B8%E7%BD%A9&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E8%83%B8%E7%BD%A9&psort=3&page={}&s=123&click=0".format(i)
            yield scrapy.Request(next_url,callback=self.parse,dont_filter=True)



    def getComments(self,productId, page):
        url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv14&productId=' + str(
            productId) + '&score=0&sortType=5&page=' + str(page) + '&pageSize=10&isShadowSku=0&fold=1'

        # yield  scrapy.Request(url,callback=self.getInfo,dont_filter=True)
    #
    # def getInfo(self,response):
        c = scrapy.Request(url)
        # r = http.request('GET', url)
        # c = r.data.decode('ISO-8859-1')
        c = c.replace('fetchJSON_comment98vv14(', '')
        c = c.replace(')', '')
        c = c.replace('false', '"false"')
        c = c.replace('true', '"true"')
        c = c.replace('null', '"null"')
        c = c.replace(';', '')
        jdDict = json.loads(c)
        return jdDict

    def getMaxPage(self,productId):
        return self.getComments(productId, 0)['maxPage']


