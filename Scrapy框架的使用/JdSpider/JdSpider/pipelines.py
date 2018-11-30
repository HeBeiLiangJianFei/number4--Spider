# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy

class JdspiderPipeline(object):
    def process_item(self, item, spider):
        return item

# class JdImagesPipeline(ImagesPipeline):
#     def process_item(self, item, spider):
#         yield scrapy.Request(url=item[''])