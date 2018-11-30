# !/usr/bin/env/python
# _*_coding:utf-8 _*_
# author:LiangJianfei
import time

from selenium import  webdriver

drowser = webdriver.Chrome()
drowser.get("http://www.baidu.com")
elem = drowser.find_element_by_id("kw")
elem.send_keys("网络爬虫")
but = drowser.find_element_by_id("su")
but.click()

time.sleep(5)
drowser.close()




