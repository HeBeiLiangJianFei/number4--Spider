'''09_selenium+Chrome登陆豆瓣案例.py'''
from selenium import webdriver
import time

# 创建浏览器对象,发请求
driver = webdriver.Chrome()
driver.get("https://www.douban.com/")
time.sleep(0.5)
# 获取截图(验证码)
driver.save_screenshot("验证码.png")
# 找 用户名、密码、验证、登陆豆瓣按钮
uname = driver.find_element_by_name("form_email")
uname.send_keys("309435365@qq.com")
# 密码
pwd = driver.find_element_by_name("form_password")
pwd.send_keys("zhanshen001")
# 验证码
key = input("请输入验证码：")
yzm = driver.find_element_by_id("captcha_field")
yzm.send_keys(key)
driver.save_screenshot("完成.png")
# 点击登陆按钮
login = driver.find_element_by_class_name("bn-submit")
login.click()
time.sleep(1)
driver.save_screenshot("登陆成功.png")
# 关闭浏览器
driver.quit()








