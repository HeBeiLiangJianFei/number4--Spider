# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BraItem(scrapy.Item):
    # define the fields for your item here like:
    SpiderName = scrapy.Field()
    content = scrapy.Field()
    productSize = scrapy.Field()
    productColor = scrapy.Field()
    creationTime = scrapy.Field()


'''
动态创建item类：
from scrapy.item import DictItem,Field
def create_item_class(class_name,field_list):
    fields = {
        field_name:Field() for field_name in field_list
    }
    return type(class_name,(DictItem,),{"fileds":fields})  
'''



