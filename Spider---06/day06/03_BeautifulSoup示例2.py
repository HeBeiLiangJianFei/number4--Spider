'''03_BeautifulSoup示例2.py'''
from bs4 import BeautifulSoup

html = '''<div class="test">雄霸</div>
          <div class="test">幽若</div>
          <div class="test2">
            <span>第二梦</span>
          </div>
       '''
soup = BeautifulSoup(html,'lxml')
# class为test的div的文本内容
divs = soup.find_all("div",attrs={"class":"test"})
for div in divs:
    print(div.string)
    print(div.get_text())
    
# class为test2的div下的span中文本内容
divs = soup.find_all("div",attrs={"class":"test2"})
for div in divs:
    print(div.span.string)
    












