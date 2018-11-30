'''07_driver.page_source.find示例.py'''
from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get("http://www.baidu.com/")

r = driver.page_source.find("ABCDEFG")
print(r)
