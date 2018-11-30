# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 定义要爬取的数据结构
class TengxunItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 职位名称
    zhName = scrapy.Field()
    # 详情链接
    zhLink = scrapy.Field()
    # 职位类别
    zhType = scrapy.Field()
    # 招聘人数
    zhNum = scrapy.Field()
    # 工作地点
    zhAddress = scrapy.Field()
    # 发布时间
    zhTime = scrapy.Field()




