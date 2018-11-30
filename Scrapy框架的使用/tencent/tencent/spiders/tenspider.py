# -*- coding: utf-8 -*-
import scrapy
from ..items import TencentItem

class TenspiderSpider(scrapy.Spider):
    name = 'tenspider'
    allowed_domains = ['hr.tencent.com']
    url = "https://hr.tencent.com/position.php?start="
    offset = 0
    start_urls = [url+str(offset)]

    def parse(self, response):
        # 获取所有页数的url
        for i in range(0,2921,10):
            yield scrapy.Request(self.url+str(i),callback=self.parseHtml)

    def parseHtml(self,response):
        result = response.xpath('//tr[@class="even"] | //tr[@class="odd"]')
        for res in result:
            item = TencentItem()
            item['jobTitle'] = res.xpath('./td[1]/a/text()').extract_first().strip()
            item['jobLink'] = "https://hr.tencent.com/"+res.xpath('./td[1]/a/@href').extract_first().strip()
            item['positionType'] = res.xpath('./td[2]/text()').extract()
            if item['positionType']:
                item['positionType'] = item['positionType']
            else:
                item['positionType'] = "无"
            item['peopleNum'] = res.xpath('./td[3]/text()').extract_first().strip()
            item['localtion'] = res.xpath('./td[4]/text()').extract_first().strip()
            item['time'] = res.xpath('./td[5]/text()').extract_first().strip()
            yield item





















