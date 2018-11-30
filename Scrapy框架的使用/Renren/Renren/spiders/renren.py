# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']

    # start_urls = ['http://renren.com/']
    # 重写start_urls方法
    def start_requests(self):
        url = "http://www.renren.com/PLogin.do"
        yield scrapy.FormRequest(url=url,formdata={"email":"13603263409","password":"zhanshen01"},callback=self.parseHtml)


    def parseHtml(self,response):
        with open("zhanshen.html",'w',encoding="utf-8") as f:
            f.write(response.text)

    # def parse(self, response):
    #     response.encoding = 'utf-8'
    #     with open("zhanshen.html",'w') as f:
    #         f.write(response.text)
