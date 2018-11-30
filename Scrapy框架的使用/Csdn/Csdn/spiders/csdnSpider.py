# -*- coding: utf-8 -*-
import scrapy
from ..items import CsdnItem

class CsdnspiderSpider(scrapy.Spider):
    name = 'csdnSpider'
    allowed_domains = ['blog.csdn.net']
    start_urls = ['http://blog.csdn.net/']

    def parse(self, response):
        # 对item.py 中的CsdnItem进行实例化
        item = CsdnItem()
        item['title'] = response.xpath('//*[@id="feedlist_id"]/li[1]/div/div[1]/h2/a/text()').extract_first().strip()
        item['time'] = response.xpath('//*[@id="feedlist_id"]/li[1]/div/dl/dd[2]/text()').extract()[0].strip()
        item['number'] = response.xpath('//*[@id="feedlist_id"]/li[1]/div/dl/div[3]/dd[1]/a/span[1]/text()').extract()[0].strip()
        yield item


