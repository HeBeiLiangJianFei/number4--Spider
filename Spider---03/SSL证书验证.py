# !/usr/bin/env/python
# _*_coding:utf-8 _*_
# author:LiangJianfei

'''SSl'''
'''SSL证书验证'''
''' verify = True : 默认，进行SSL证书认证
    verify = False 不做认证
        
'''

import requests

# url = "http://www.12306.cn/mormhweb/"
url = "https://www.12306.cn/mormhweb/"
headers = {"User-Agent":"Mozilla/5.0"}

res = requests.get(url,headers=headers,verify = False)

print(res.status_code)

