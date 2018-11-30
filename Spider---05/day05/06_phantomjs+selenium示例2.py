'''06_phantomjs+selenium示例2.py'''
from selenium import webdriver
import time

# 创建浏览器对象
driver = webdriver.PhantomJS()
# 打开页面
driver.get("http://www.baidu.com/")
# 发送文字到搜索框
kw = driver.find_element_by_id("kw")
kw.send_keys("美女")
# 点击 "百度一下"
su = driver.find_element_by_id("su")
su.click()
time.sleep(1)
# 获取截屏
driver.save_screenshot("美女.png")
# 关闭浏览器
driver.quit()









