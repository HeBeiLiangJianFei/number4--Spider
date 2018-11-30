'''07_cookie模拟登陆人人网.py'''
import urllib.request

url = "http://www.renren.com/967469305/profile"
headers = {
        "Host":"www.renren.com",
        "Connection":"keep-alive",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Referer":"http://www.renren.com/",
#        Accept-Encoding: gzip, deflate
        "Accept-Language":"zh-CN,zh;q=0.9",
        "Cookie":"anonymid=jnoaljpk7d3nh2; depovince=BJ; _r01_=1; _de=4DBCFCC17D9E50C8C92BCDC45CC5C3B7; ln_uact=13603263409; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebe_key=1b1f4a34-0468-4185-a3b0-6f2c38abc368%7C2012cb2155debcd0710a4bf5a73220e8%7C1540454149943%7C1%7C1540454153787; wp_fold=0; wp=0; jebecookies=2fc339e7-1b51-43ce-bc85-e2dc1f68ee16|||||; JSESSIONID=abcANrnqoMuLshY34pQAw; ick_login=30d0bd58-f6bb-437f-8d0d-6a72ae00e7b7; p=1e1b85cb8dda387a70e400a341c2e9c95; first_login_flag=1; t=4f652cc0a8f3fd50f5c9095c92d4717d5; societyguester=4f652cc0a8f3fd50f5c9095c92d4717d5; id=967469305; xnsid=55bff2d5; loginfrom=syshome"
    }

req = urllib.request.Request(url,headers=headers)
res = urllib.request.urlopen(req)
print(res.read().decode("utf-8"))















