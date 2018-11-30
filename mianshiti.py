# !/usr/bin/env/python
# _*_coding:utf-8 _*_
# author:LiangJianfei



rs = [1,2,3,4,5,6,7,8,9,10]
a = 1
b = 0
bs = []
while True:
    print(a)

    if b == 10:
        b = 0

    if a == 4:
        a = 1
        bs.append(rs[b])
    a = a + 1

    b = b + 1
    if len(bs) != 9:
        print(rs[b])
        break

