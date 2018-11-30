# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import *
class DouyuspiderSpider(scrapy.Spider):
    name = 'douyuspider'
    # allowed_domains = ['capi.douyucdn.cn']
    allowed_domains = ['douyucdn.com']
    baseurl = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
    offset = 0
    start_urls = [baseurl+str(offset)]

    def parse(self, response):
        dic = json.loads(response.text)['data']
        if not dic:
            return
        item = DouyuItem()
        for i in dic:
            item['vertical_src'] = i['vertical_src']
            item['room_id'] = i['room_id']
            item['nickname'] = i['nickname']
            item['anchor_city'] = i['anchor_city']
            yield item
        self.offset += 20
        next = self.baseurl+str(self.offset)
        url = response.urljoin(next)
        # print("url-------->",url)
        yield scrapy.Request(url=url, meta={'item': item}, callback=self.parse, dont_filter=True)
        # yield scrapy.Request(url,callback=self.parse)
        # yield scrapy.Request(next,callback=self.parse)
