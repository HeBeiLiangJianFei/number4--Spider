# !/usr/bin/env/python
# _*_coding:utf-8 _*_
# author:LiangJianfei

def  fib(n):
    a,b,s, = 0,1,0
    while s < n:
        a,b = b,a+b
        # print(b,end='->')
        s += 1
        yield b


if __name__ == "__main__":
    print("程序开始。。。")
    n = int(input("请输入："))
    for i in fib(n):
        print(i)
        print(type(i))



