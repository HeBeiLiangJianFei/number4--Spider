# -*- coding: utf-8 -*-
import scrapy


class LianjiaspiderSpider(scrapy.Spider):
    name = 'lianjiaspider'
    allowed_domains = ['lianjia.com']
    start_urls = ['http://lianjia.com/']

    def parse(self, response):
        pass
