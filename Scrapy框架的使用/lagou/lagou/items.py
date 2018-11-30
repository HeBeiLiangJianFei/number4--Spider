# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jobName = scrapy.Field()
    jobAddres = scrapy.Field()
    compName = scrapy.Field()
    salary = scrapy.Field()
    exprience = scrapy.Field()
    scale = scrapy.Field()
    treatment = scrapy.Field()
