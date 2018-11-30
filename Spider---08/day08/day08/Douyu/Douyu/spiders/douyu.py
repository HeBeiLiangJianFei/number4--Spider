# -*- coding: utf-8 -*-
import scrapy
import json
from Douyu.items import DouyuItem

class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['douyucdn.cn']
    baseurl = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    offset = 0

    start_urls = [baseurl + str(offset)]

    def parse(self, response):
        # r_list存放所有主播信息,每个主播为一个字典
        r_list = json.loads(response.text)['data']
        if len(r_list) == 0:
            return 

        for r in r_list:
            item = DouyuItem()
            item['link'] = r['vertical_src']
            item['name'] = r['nickname']
            item['house'] = r['room_id']
            item['city'] = r['anchor_city']

            yield item

        self.offset += 20
        yield scrapy.Request(self.baseurl+str(self.offset),callback=self.parse,dont_filter=True)
        

