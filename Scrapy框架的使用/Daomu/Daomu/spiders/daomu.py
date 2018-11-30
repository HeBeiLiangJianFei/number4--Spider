# -*- coding: utf-8 -*-
import scrapy
from ..items import DaomuItem

class DaomuSpider(scrapy.Spider):
    name = 'daomu'
    allowed_domains = ['daomubiji.com']
    start_urls = ['http://www.daomubiji.com/dao-mu-bi-ji-1']

    def parse(self, response):
        item = DaomuItem()
        item['bookName'] = response.xpath('/html/body/div[1]/div/h1/text()').extract_first().strip()
        articles = response.xpath('//article[@class="excerpt excerpt-c3"]')
        for article in articles:
            info = article.xpath('./a/text()').extract()[0].strip().split(' ')
            item['bookTitle'] = info[0]
            item['bookChapter'] = info[2]
            item['chapterNum'] = info[1]
            item['chapterHref'] = article.xpath('./a/@href').extract_first()
            yield item
