# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    
    # 重写Spider类的start_requests()方法,start_urls去掉
    def start_requests(self):
        url = "http://www.renren.com/PLogin.do"
        # FormRequest()方法把Form表单数据发送给服务器
        yield scrapy.FormRequest(url=url,
            formdata={"email":"13603263409","password":"zhanshen001"},
            callback=self.parseHtml)


    def parseHtml(self, response):
        with open("zhanshen.html","w") as f:
            f.write(response.text)





