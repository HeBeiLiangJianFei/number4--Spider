'''05_phantomjs+selenium示例1.py'''
# 导入selenium库中的webdriver接口
from selenium import webdriver

# 创建phantomjs浏览器对象
driver = webdriver.PhantomJS()
# 发请求 get()
driver.get("http://www.baidu.com/")
print(driver.page_source)
## 获取网页截屏
#driver.save_screenshot("百度.png")
#print("图片保存成功")
## 关闭
#driver.quit()














