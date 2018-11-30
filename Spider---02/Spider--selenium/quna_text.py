# !/usr/bin/env/python
# _*_coding:utf-8 _*_
# author:LiangJianfei
import codecs
import datetime
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class QunaSpider(object):

    def get_hotel(self,driver,to_city,fromdate,todate):
        ele_toCity = driver.find_element_by_name("toCity")
        ele_fromDate = driver.find_element_by_id("fromDate")
        ele_toDate = driver.find_element_by_id("toDate")
        ele_search = driver.find_element_by_class_name("search-btn")
        ele_toCity.clear()
        ele_toCity.send_keys(to_city)
        ele_fromDate.clear()
        ele_fromDate.send_keys(fromdate)
        ele_toDate.clear()
        ele_toDate.send_keys(todate)
        ele_search.click()
        page_num =0
        while 1:
            try:
                WebDriverWait(driver,10).until(EC.title_contains(to_city))
            except Exception as e:
                print("出错111：",e)
                driver.close()
                break


            time.sleep(5)
            js = "window.scrollTo(0,document.body.scrollHeight);"
            driver.execute_script(js)
            time.sleep(5)

            # 获取网页源码
            # htm_const = driver.page_source
            # soup = BeautifulSoup(htm_const,"html.parser",from_encoding="utf-8")
            # infos = soup.find_all(class_="item_hotel_info")
            # f = codecs.open(to_city+fromdate+".html","a","utf-8")
            # for info in infos:
            #     f.writer(str(page_num)+"--"*50)
            #     content = info.get_text().replace(" ","").replace("\t","").strip()
            #     for line in [Ln for Ln in content.splitlines() if Ln.strip()]:
            #         f.writer(line)
            #         f.writer("\r\n")
            # f.close()
            try:
                # next_page = WebDriverWait(driver,4).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.item next')))
                next_page = driver.find_element_by_css_selector(".item.next")
                next_page.click()
                page_num += 1
                time.sleep(10)
            except Exception as e:
                print("出错222：",e)
                driver.close()
                break






    def crawl(self,root_url,to_city):
        today = datetime.date.today().strftime("%Y-%m-%d")
        tomorrow =datetime.date.today() +datetime.timedelta(days=1)
        tomorrow = tomorrow.strftime("%Y-%m-%d")
        driver = webdriver.Chrome()
        driver.set_page_load_timeout(50)
        driver.get(root_url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        self.get_hotel(driver,to_city,today,tomorrow)


if __name__ == "__main__":
    spider = QunaSpider()
    spider.crawl("http://hotel.qunar.com/","上海")