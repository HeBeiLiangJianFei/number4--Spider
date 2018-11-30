# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    # 图片链接
    link = scrapy.Field()
    name = scrapy.Field()
    house = scrapy.Field()
    city = scrapy.Field()












