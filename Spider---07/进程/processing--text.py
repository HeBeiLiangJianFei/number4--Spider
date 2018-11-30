# !/usr/bin/env/python
# _*_coding:utf-8 _*_
# author:LiangJianfei


from multiprocessing import Process
from multiprocessing import Pool

class lianSpider(object):
    def myProcess(self):
        print("myProcess  Spider 程序运行中  运行中...")

    def run2(self):
        self.myProcess()

# ls = lianSpider()
# p1 = Process(target=myProcess,)
def run():
    p = Pool(processes=5)
    result = []
    for i in range(20):
        pro = p.apply_async(lianSpider().run2,)
        result.append(pro)
    p.close()

    p.join()
    for i in result:
        print(i)


if __name__ == "__main__":
    # p1.start()
    # p1.join()
    run()