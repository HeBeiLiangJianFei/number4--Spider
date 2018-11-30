# !/usr/bin/env/python
# _*_coding:utf-8 _*_
# author:LiangJianfei

from fake_useragent import UserAgent

class Ran(object):
    def __init__(self):
        pass
    def random_useragent(self):
        ua = UserAgent()
        dic = {}
        dic['User-Agent'] = ua.chrome
        return dic

