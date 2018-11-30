# -*- coding: utf-8 -*-
import scrapy
from ..items import *

class FeijiuSpider(scrapy.Spider):
    name = 'feijiu'
    allowed_domains = ['feijiu.net']
    start_urls = ['http://feijiu.net/']

    item = FeijiuItem()
    def parse(self, response):
        li_lis = response.xpath('//div[@class="list"]/ul/li')
        for li in li_lis:

            li_text = li.xpath('./a/text()').extract_first()
            li_url = li.xpath('./a/@href').extract_first()

            self.item['li_text'] = li_text
            self.item['li_url'] = li_url
            yield scrapy.Request(url=li_url,callback=self.next_parse,meta={'li_text':li_text,'li_url':li_url},dont_filter=True)

    def next_parse(self,response):
        next_lis = response.xpath('//div[@class="ej_l"]/div/h5/a[1]')
        for next in next_lis:
            next_url = next.xpath('./@href').extract_first()
            next_text = next.xpath('./text()').extract_first()
            self.item['li_url'] = response.meta.get('li_url')
            self.item['li_text'] = response.meta.get('li_text')
            self.item['next_url'] = next_url
            self.item['next_text'] = next_text
            yield self.item
