# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from lxml import etree
from ..items import *


class LagspiderSpider(scrapy.Spider):
    name = 'lagspider'
    allowed_domains = ['lagou.com']
    start_urls = ['https://www.lagou.com/zhaopin/Python/']

    def parse(self, response):
        return scrapy.Request(url=self.start_urls[0], callback=self.get_html,)

    def get_html(self,response):
        broswer = webdriver.Chrome()
        broswer.get(self.start_urls[0])
        html = broswer.page_source
        result = etree.HTML(html)
        jobNames = result.xpath('//div[@class="p_top"]/a/h3/text()')
        jobAddress = result.xpath('//div[@class="p_top"]/a/span/em/text()')
        compNames = result.xpath('//div[@class="company_name"]/a/text()')
        salarys = result.xpath('//div[@class="p_bot"]/div/span/text()')
        expriences = result.xpath('//div[@class="p_bot"]/div/text()[3]')
        scales = result.xpath('//div[@class="industry"]/text()')
        treatments = result.xpath('//div[@class="list_item_bot"]/div[2]/text()')
        item = LagouItem()
        for jobName,jobAddres,compName,salary,exprience,scale,treatment in zip(jobNames,jobAddress,compNames,salarys,expriences,scales,treatments):
            item['jobName'] = jobName.strip()
            item['jobAddres'] = jobAddres
            item['compName'] = compName
            item['salary'] = salary
            item['exprience'] = exprience
            item['scale'] = scale
            item['treatment'] = treatment
            yield item

    def next_page(self,response):
        pass


