'''08_driver.find查找元素示例.py'''
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.qiushibaike.com/")

# 查找单个节点 element
r_One = driver.find_element_by_class_name("content")
print(r_One.text)

# 查找多个节点 elements
r_Many = driver.find_elements_by_class_name("content")
for r in r_Many:
    print(r.text)
    print()

driver.quit()















