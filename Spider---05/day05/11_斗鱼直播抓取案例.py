'''11_斗鱼直播抓取案例.py'''
from selenium import webdriver
from lxml import etree
import time

# 把Chrome设置无界面浏览器
# opt = webdriver.ChromeOptions()
# opt.set_headless()
# 创建浏览器对象,发请求
# driver = webdriver.Chrome(options=opt)
driver = webdriver.Chrome()
driver.get("https://www.douyu.com/directory/all")
i = 1


# 循环
while i<2:
    # 解析(driver.page_source)
    # 获取主播名称 和 观众人数
    parseHtml = etree.HTML(driver.page_source)
    # names = parseHtml.xpath('//div[@id="live-list-content"]//span[@class="dy-name ellipsis fl"]')
    names = parseHtml.xpath('//*[@id="live-list-contentbox"]/li/a/div/p/span[1]')
    numbers = parseHtml.xpath('//div[@id="live-list-content"]//span[@class="dy-num fr"]')
    num = parseHtml.xpath('//*[@id="live-list-contentbox"]/li/a/div/p/span[@class="dy-num fr"]')
    print(num)
    # for name,number in zip(names,numbers):
    for name,number in zip(names,num):
        print("\t主播名称：%s \t观众人数：%s" %
              (name.text.strip(),number.text.strip()))
        #for name,number in [("主播1","20万"),("主播2","15万")]
    print("第%d页爬取成功" % i)
    i += 1
    # 判断是否需要点击下一页
    # 能点 ：点击,继续循环
    # print(driver.page_source.find("shark-pager-next shark-pager-disable shark-pager-disable-next"))
    if driver.page_source.find("shark-pager-next shark-pager-disable shark-pager-disable-next") == -1:
        driver.find_element_by_class_name("shark-pager-next").click()
        time.sleep(1)
    else:
        break
    # 不能点 ：break0

print("一共爬取了%d页" % i)



















