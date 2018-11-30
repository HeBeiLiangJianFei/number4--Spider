# !/usr/bin/env/python
# _*_coding:utf-8 _*_
# author:LiangJianfei

'''线程'''
'''
    1、进程中包含多个线程，1个进程可包含多个线程
    2、线程可使用所属进程的空间（有自己独立的堆栈空间，但数据共享，同一时间内一次只能执行1个线程，其他
    阻塞等待）
    3、锁：防止多个线程同时使用同一个进程的共享空间
    4、GIL全局解释锁：
        程序执行的通行证，仅有一个；拿到通行证以后才能去执行，否则，只能等待
    5、应用场景：
        1、多进程：要稳定不要速度，大量的密集型计算
        2、多线程：要速度，I/O密集型的计算。
    
    
'''

'''爬取百思不得琪姐的段子
    1、目标：段子内容
    2、url:http://www.budejie.com/
    3、根据xpath表达式获取文本内容：/html/body/div[3]/div/div[2]/div[1]/div[2]/ul/li/div[2]/div[1]/a
        //div[@class="j-r-list-c-desc"/a/text()
    4、知识点：
        1、队列（from queue import Queue)
            put()
            get()
            Queue.empty():判断队列时候为空
            Queue.join():如果队列为空，执行其他程序
        2、线程（import threading)
            threading.Thread(target="..")
            
'''


from threading import Thread
import requests
from lxml import etree
from queue import Queue
import time


class BsSpider(object):

    def __init__(self,):
        self.baseurl = "http://www.budejie.com/"
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
        # 初始化url队列
        self.urlQueue = Queue()
        # 初始化HTML响应队列
        self.htmlQueue = Queue()

    # 生成一个url队列
    def getUrl(self):
        for page in range(1,50):
            url = self.baseurl+str(page)
            # 将拼接好的url放入队列中
            self.urlQueue.put(url)

    # 网页text队列
    def getHtml(self):
        while True:
            # 在url队列中取出一个url
            url = self.urlQueue.get()
            resp = requests.get(url,headers = self.headers)
            resp.encoding = "utf-8"
            html = resp.text
            # 将HTML放入HTML队列中
            self.htmlQueue.put(html)
            # 清除次任务
            self.urlQueue.task_done()


    # 解析HTML
    def getInfo(self):
        while True:
            html = self.htmlQueue.get()
            result = etree.HTML(html)
            datas = result.xpath('//div[@class="j-r-list-c-desc"]/a/text()')
            for i in datas:
                print("内容：",i)
            # 清除任务
            self.htmlQueue.task_done()

    def run(self):
        # 定义一个空列表,存放所有的线程
        thread_list = []
        self.getUrl()
        for i in range(4):
            threadRes = Thread(target=self.getHtml)
            thread_list.append(threadRes)
        print(thread_list)

        for i in range(4):
            threadResult = Thread(target=self.getInfo)
            thread_list.append(threadResult)
        print(thread_list)

        for th in thread_list:
            # 设置为守护线程
            th.setDaemon(True)
            th.start()

        self.urlQueue.join()
        self.htmlQueue.join()
        print("运行结束")



if __name__ == "__main__":
    start = time.time()
    # print(start)
    spider = BsSpider()
    # print("spider实例化成功")
    spider.run()
    # print("spider running...")
    end = time.time()
    print("程序用时:",(end-start))

















