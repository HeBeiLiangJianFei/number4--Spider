'''10_driver操作键盘示例.py'''
from selenium import webdriver
# 操作键盘
from selenium.webdriver.common.keys import Keys
import time

# 创建浏览器对象,发请求
driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")
# 百度搜索框输入python
kw = driver.find_element_by_id("kw")
kw.send_keys("python")
driver.save_screenshot("01_python.png")

# 全选 ：Ctrl + a
kw = driver.find_element_by_id("kw")
kw.send_keys(Keys.CONTROL,'a')
driver.save_screenshot("02_CtrlA.png")

# 剪切 ：Ctrl + x
kw = driver.find_element_by_id("kw")
kw.send_keys(Keys.CONTROL,'x')
driver.save_screenshot("03_CtrlX.png")

# 粘贴 ：Ctrl + v
kw = driver.find_element_by_id("kw")
kw.send_keys(Keys.CONTROL,'v')
driver.save_screenshot("04_CtrlV.png")

# 清空搜索框 : 对象名.clear()
kw = driver.find_element_by_id("kw")
kw.clear()
driver.save_screenshot("05_Clear.png")

# 输入 ：达内科技
kw = driver.find_element_by_id("kw")
kw.send_keys("达内科技")
driver.save_screenshot("06_Tarena.png")

# 输入 ：回车
kw = driver.find_element_by_id("kw")
kw.send_keys(Keys.ENTER)
time.sleep(1)
driver.save_screenshot("07_Enter.png")

# 关闭浏览器
driver.quit()







