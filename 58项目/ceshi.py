# !/usr/bin/env/python
# _*_coding:utf-8 _*_
# author:LiangJianfei
# from Random_UA import Ran

# from channel_extract import get_channel_urls

from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from Random_UA import Ran
import requests

start_url = "https://bj.58.com/sale.shtml"
url_host = "https://bj.58.com"
# headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36"}
def get_channel_urls(url):
    headers = Ran().random_useragent()
    wb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    links = soup.select('ul.ym-submnu > li > span > a')
    channel_urls = ''
    for link in links:
        page_url = url_host + link.get("href")
        channel_urls += page_url
        channel_urls += "\n"
    return channel_urls

channel_list = get_channel_urls(start_url)

from multiprocessing import Pool

def fun(url):
    print(url)


if __name__ == "__main__":
    pool = Pool()
    pool.map(fun,channel_list.split("\n"))


# import pymongo
#
# client = pymongo.MongoClient("localhost",27017)
# ceshi = client['ceshi']
# url_list = ceshi['url_list3']
#
# cursor = url_list.find({},{"_id":0})
# cursor.limit(2000)
# for i in cursor:
#     print(i['url'])


# if __name__ == "__main__":
#     split_urls()


# st = '''
# https:https://jumpzhineng.58.com/jump
# https:https://jumpzhineng.58.com/jump
# https:https://jumpzhineng.58.com/jump
# https:https://jumpzhineng.58.com/jump
# https:https://jumpzhineng.58.com/jump
# https:https://jumpzhineng.58.com/jump
# https:https://jumpzhineng.58.com/jump
# https:https://jumpzhineng.58.com/jump
# https:http://zhuanzhuan.58.com/detail/971920119891476489z.shtml
# https:http://zhuanzhuan.58.com/detail/1021666375915799052z.shtml
# https:http://zhuanzhuan.58.com/detail/1062272245840019468z.shtml
# https:http://zhuanzhuan.58.com/detail/1061117985288454163z.shtml
# https:http://zhuanzhuan.58.com/detail/1059010088150859785z.shtml
# https:https://jumpzhineng.58.com/jump
# https:http://zhuanzhuan.58.com/detail/1060122390527426571z.shtml
# https:http://zhuanzhuan.58.com/detail/1063563595034148876z.shtml
# https:http://zhuanzhuan.58.com/detail/1043078118608421378z.shtml
# https:http://zhuanzhuan.58.com/detail/1061939637063712769z.shtml
# https:http://zhuanzhuan.58.com/detail/1053964527971909640z.shtml
# https:https://jumpzhineng.58.com/jump
# https:http://zhuanzhuan.58.com/detail/907453396385415176z.shtml
# https:http://zhuanzhuan.58.com/detail/967345538775547911z.shtml
# https:http://zhuanzhuan.58.com/detail/1055998092328894475z.shtml
# https:http://zhuanzhuan.58.com/detail/1044821080036884493z.shtml
# https:http://zhuanzhuan.58.com/detail/1028186378467803155z.shtml
# https:https://jumpzhineng.58.com/jump
# https:http://zhuanzhuan.58.com/detail/993640699308621828z.shtml
# https:http://zhuanzhuan.58.com/detail/805226174662721542z.shtml
# https:http://zhuanzhuan.58.com/detail/972639703448813575z.shtml
# https:http://zhuanzhuan.58.com/detail/1063040616138768392z.shtml
# https:http://zhuanzhuan.58.com/detail/1056531449320570899z.shtml
# https:http://zhuanzhuan.58.com/detail/998070857323102211z.shtml
# https:http://zhuanzhuan.58.com/detail/860833202289983494z.shtml
# https:http://zhuanzhuan.58.com/detail/1043457172217610260z.shtml
# https:http://zhuanzhuan.58.com/detail/1062282823902511105z.shtml
# https:http://zhuanzhuan.58.com/detail/1014101619714408452z.shtml
# '''
# for i in st.split('\n'):
#     if "detail" in i:
#         print("st")
#     else:
#         print("lt")
#     print()
