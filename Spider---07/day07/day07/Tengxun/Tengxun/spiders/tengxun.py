# -*- coding: utf-8 -*-
import scrapy
from Tengxun.items import TengxunItem

class TengxunSpider(scrapy.Spider):
    name = 'tengxun'
    allowed_domains = ['tencent.com']
    # 定义基准url,方便下面做url拼接
    url = "https://hr.tencent.com/position.php?&start="
    offset = 0
    # 只是最开始的url
    start_urls = [url + str(offset)]

    def parse(self, response):
        # 把293页的URL都给引擎,引擎给调度器去入队列,再给下载器
        for i in range(0,2921,10):
            yield scrapy.Request(self.url+str(i), \
                                 callback=self.parseHtml)

    def parseHtml(self,response):
        # 每个职位节点对象列表
        base_list = response.xpath('//tr[@class="even"] | //tr[@class="odd"]')
        for base in base_list:
            item = TengxunItem()
            item['zhName'] = base.xpath('./td[1]/a/text()').extract()[0]
            item['zhLink'] = base.xpath('./td[1]/a/@href').extract()[0]         
            
            item['zhType'] = base.xpath('./td[2]/text()').extract()
            if item['zhType']:
                item['zhType'] = item['zhType'][0]
            else:
                item['zhType'] = "无"

            item['zhNum'] = base.xpath('./td[3]/text()').extract()[0]
            item['zhAddress'] = base.xpath('./td[4]/text()').extract()[0]
            item['zhTime'] = base.xpath('./td[5]/text()').extract()[0]

            yield item

