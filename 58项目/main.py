# !/usr/bin/env/python
# _*_coding:utf-8 _*_
# author:LiangJianfei

from multiprocessing import Process,Pool
from channel_extract import channel_list
from page_parsing import get_links_from


def get_all_links_from(channel):
    for num in range(1,101):
        get_links_from(channel,num)



if __name__ == "__main__":
    pool = Pool()
    pool.map(get_all_links_from,channel_list.split("\n"))




















