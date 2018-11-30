# -*- coding: utf-8 -*-
import scrapy
from Daomu.items import DaomuItem

class DaomuSpider(scrapy.Spider):
    name = 'daomu'
    allowed_domains = ['daomubiji.com']
    start_urls = ['http://www.daomubiji.com/dao-mu-bi-ji-1']

    def parse(self, response):
        # 创建item对象(items.py里面的class)
        item = DaomuItem()
        # 匹配书名(单独匹配)
        item["bookName"] = response.xpath('//h1[@class="focusbox-title"]/text()').extract()[0]
        # 匹配所有章节对象(基准xpath)
        articles = response.xpath('//article[@class="excerpt excerpt-c3"]')
        for article in articles:
            info = article.xpath('./a/text()').extract()[0].split(' ')
            # ['七星鲁王','第十二章','门']
            item["bookTitle"] = info[0]
            item["zhName"] = info[2]
            item["zhNum"] = info[1]
            item["zhLink"] = article.xpath('./a/@href').extract()[0]

            yield item
        
