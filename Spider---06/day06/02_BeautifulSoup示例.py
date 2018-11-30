'''02_BeautifulSoup示例.py'''
from bs4 import BeautifulSoup

html = '<div class="test">雄霸</div>'
# 创建解析对象
soup = BeautifulSoup(html,'lxml')
# 查找节点
#r_list = soup.find_all(class_="test")
r_list = soup.find_all("div",attrs={"class":"test"})

for r in r_list:
    print(r.get_text())



















