# !/usr/bin/env/python
# _*_coding:utf-8 _*_
# author:LiangJianfei

''''''
import time

'''
01、解决动态网页爬取
02、伪造报文头、IP代理----最厉害的反爬就是验证码
03、图像识别、机器学习 
04、分布式爬虫、内存数据库
05、自然语言处理技术---jieba分词
06、数据库存储


通用框架：   
    信息采集
    索引检索
    web接口可视化
    
www --> 多个spider --->原始文档库--->索引--->索引库--->检索-->用户接口-->可视化

聚焦爬虫：
    通过搜索返回太多用户不关心
    服务器资源，而网络数据资源无限
    网络资源多样化，通用爬虫模型无法很好获取
    关键系匹配技术无法识别语意
 

从scrapy看聚焦爬虫框架：
       
编程和打架一样，谁先动手谁就输了

项目开发流程：
    
加速爬虫：
    异步加载： Asynico
    异步非阻塞
    
    
    
    
    
'''
# import json
# a = '{"a":1}'
# print(json.loads(a)['a'])

import asyncio
# async  def job(t):
#     print("Start job",t)
#     await asyncio.sleep(t)
#     print("Job",t,"Takes",t,' s')
#
# async  def main(loop):
#     tasks = [loop.create_task(job(t)) for t in range(1,4)]
#     await asyncio.wait(tasks)
#
# t1 = time.time()
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main(loop))
# print("Async time",time.time()-t1)


# import aiohttp
#
# URL = "https://www.baidu.com"
# async def job1(session):
#     response = await session.get(URL)
#     return str(response.url)
#
# async def main(loop):
#     async with aiohttp.ClientSession() as session:
#         tasks = [loop.create_task(job1(session)) for _ in range(2)]
#         finised,unfinised = await asyncio.wait(tasks)
#         all_result = [r.result() for r in finised]
#         print(all_result)
#
# t1 = time.time()
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main(loop))
# print("asd time",time.time() - t1)

#
# def add(n,i):
#     return n + i
#
# def test():
#     for i in range(4):
#         yield i
#
# g = test()
# for n in [1,10]:
#     g = (add(n,i) for i in g)
#
#
# print(list(g))



# ret = zip((("a"),("b")),(("c"),("d")))
#
# def func(tup):
#     return {tup[0]:tup[1]}
#
#
#
# # res = list(map(func,ret))
#
#
# res = list(map(lambda tup:{tup[0]:tup[1]},ret))
#
# print(res)

def mul():
    return [lambda x:i*x for i in range(4)]

print([m(2) for m in mul()])


















