# !/usr/bin/env/python
# _*_coding:utf-8 _*_
# author:LiangJianfei


# import requests
# import re
# from lxml import etree
#
#
# headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"}
# url = "https://tj.58.com/chuzu/"
#
# rep = requests.get(url,headers=headers)
# rep.encoding ="utf-8"
#
# # pat = re.compile('<a.*?class="strongbox".*?rel="nofollow" >(.*?)</a>.*?<em>',re.S)
# # text = re.findall(pat,rep.text)
# html = etree.HTML(rep.text)
# text = html.xpath('.//div[@class="content"]/li/h2/a/text()')
#
#
# print(text)
# print(len(text))
#
# def fun(x):
#     return x+2
#
#
# # map(func,iterable)
# print(tuple(map(fun,[1,2,3,4])))


# import math
# #
# # def is_sqrt(x):
# #     return math.sqrt(x)%1 == 0
# #
# # # filter(function,iterable)
# # print(list(filter(is_sqrt,range(100))))

# arry = ['Tom', 'Jerry', 'Spike', 'Tyke']
#
# print(sorted(arry,key=len))
# print(sorted(arry,key=lambda x:len(x)))


# 递归函数：
#
# def mysum(x):
#     if x == 1:
#         return x
#     else:
#         return x + mysum(x-1)
#
# print(mysum(5))
#
#
# def fibo(n):
#     if n<=1:
#         return n
#     else:
#         return (fibo(n-1)+fibo(n-2))
#
# n = int(input("请输入："))
# if n<=0:
#     print("请输入正确的数列")
# else:
#     for i in range(n):
#         print(fibo(i),end="--")


'''
闭包的三大特征：
1、闭包函数必须内嵌函数
2、内嵌函数必须引用外部函数的变量
3、闭包函数必须返回与一个函数

闭包执行完毕后任然能够保持当前的运行环境
闭包可以根据外部作用域的局部变量来得到不同的结果，我们可以
根据修改外部变量，得到不同的功能

'''

def count(x):
    fx = []
    for i in range(1,4):
        def f(a):
            return i*x+a
        fx.append(f)
    return fx

print(count(2))

f1,f2,f3 = count(2)
print(f1(1),f2(2),f3(3))







