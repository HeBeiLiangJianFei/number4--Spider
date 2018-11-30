# -*- coding: utf-8 -*-
import scrapy
# from 包名.模块名 import 类名
from Csdn.items import CsdnItem

class CsdnSpider(scrapy.Spider):
    # 爬虫名,运行爬虫时使用
    name = 'csdn'
    # 域
    allowed_domains = ['blog.csdn.net']
    # 起始url
    start_urls = ['https://blog.csdn.net/qq_42231391/article/details/83506181']

    def parse(self, response):
        item = CsdnItem()
        # response.xpath('...') 得到选择器对象(节点所有内容) [<selector ...,data='<h1>...</h1>']
        # response.xpath('.../text()') 得到选择器对象(节点文本) [<selector ...,data='文本内容'>]
        # extract() : 把选择器对象中的文本取出来 ['文本内容']
        
        item["name"] = response.xpath('//h1[@class="title-article"]/text()').extract()[0]
        item["time"] = response.xpath('//span[@class="time"]/text()').extract()[0]
        item["number"] = response.xpath('//span[@class="read-count"]/text()').extract()[0]
        
        yield item

