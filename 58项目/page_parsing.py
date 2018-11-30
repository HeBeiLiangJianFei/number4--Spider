# !/usr/bin/env/python
# _*_coding:utf-8 _*_
# author:LiangJianfei
import random

from bs4 import BeautifulSoup
import requests
import time
import pymongo
from fake_useragent import UserAgent
from Random_UA import Ran
client = pymongo.MongoClient('localhost',27017)
ceshi = client['ceshi']
url_list = ceshi['url_list3']
item_info = ceshi['item_info3']

# 获取商品的连接

def get_links_from(channel, pages, who_sells=0):
    list_view = '{}{}/pn{}/'.format(channel,str(who_sells),str(pages))
    headers = Ran().random_useragent()
    wb_data = requests.get(list_view,headers=headers)
    time.sleep(random.randint(1,3))
    soup = BeautifulSoup(wb_data.text,"lxml")

    if soup.find('td','t'):
        for link in soup.select('td.t a.t'):
            item_link = link.get("href").split("?")[0]
            if "detail" in item_link and ("http:" in item_link or "https:" in item_link):
                url_list.insert_one({"url":item_link})
                print(item_link)
            else:
                pass
            # url_list.insert_one({"url": item_link})
            # print(item_link)

    else:
        pass

def get_item_info(url):
    headers = Ran().random_useragent()
    wb_data = requests.get(url,headers = headers)
    soup = BeautifulSoup(wb_data.text,"lxml")
    no_longer_exist = '404' in soup.find('script', node_type="text/javascript").get('src').split('/')
    if no_longer_exist:
        pass
    else:
        title = soup.title.text
        price = soup.select('span.price.c_f50')[0].text
        date = soup.select('.time')[0].text
        area = list(soup.select('.c_25d a')[0].stripped_strings) if soup.find_all('span','c_25d') else None
        item_info.insert_one({
            'title':title,
            'price':price,
            'date':date,
            'area':area
        })
        print({
            'title':title,
            'price':price,
            'date':date,
            'area':area
        })





