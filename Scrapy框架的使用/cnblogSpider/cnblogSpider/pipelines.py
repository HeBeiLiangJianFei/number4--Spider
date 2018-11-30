# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import json
import csv
from scrapy.exceptions import DropItem


class CnblogspiderPipeline(object):

    def __init__(self):
        self.file = open("papers.json","wb")

    def process_item(self, item, spider):
        if item["title"]:
            line = json.dumps(dict(item),ensure_ascii=False) + "\n"
            self.file.write(line)
            return item
        else:
            raise DropItem("Missing title in %s"%item)


    # def writeCsv(self,r_list):
    #     with open("博客.csv","a",newline="",encoding="UTF-8") as f:
    #         writer = csv.writer(f)
    #         writer.writerow(r_list)