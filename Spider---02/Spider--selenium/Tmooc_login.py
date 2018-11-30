# !/usr/bin/env/python
# _*_coding:utf-8 _*_
# author:LiangJianfei



# from selenium import webdriver
# import time
# '''模拟浏览器登录Tmooc,进行账号密码登录'''
# def loginSimulation():
#     browser = webdriver.Chrome()
#     browser.get("http://www.tmooc.cn/")
#     login = browser.find_element_by_id("login_xxw")
#     login.click()
#     time.sleep(0.4)
#     email = browser.find_element_by_id("js_account_pm")
#     pwd = browser.find_element_by_id("js_password")
#     but = browser.find_element_by_id("js_submit_login")
#     email.send_keys("1436678918@qq.com")
#     pwd.send_keys("20320342")
#     but.click()
#
#     time.sleep(7)
#     browser.close()


from selenium import webdriver
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

'''模拟浏览器登录Tmooc,进行账号密码登录'''
def loginSimulation():
    browser = webdriver.Chrome()
    browser.get("http://www.tmooc.cn/")
    login = browser.find_element_by_id("login_xxw")
    login.click()
    time.sleep(0.4)
    wait = WebDriverWait(browser,3)
    email = wait.until(EC.presence_of_element_located((By.ID,"js_account_pm")))
    # email = browser.find_element_by_id("js_account_pm")
    pwd = wait.until(EC.presence_of_element_located((By.ID,"js_password")))
    # pwd = browser.find_element_by_id("js_password")
    but = wait.until(EC.presence_of_element_located((By.ID,"js_submit_login")))
    # but = browser.find_element_by_id("js_submit_login")

    email.send_keys("1436678918@qq.com")
    pwd.send_keys("20320342")
    but.click()

    time.sleep(7)
    browser.close()

if __name__ =="__main__":
    loginSimulation()