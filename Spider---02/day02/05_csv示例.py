'''05_csv示例.py'''
import csv

with open("猫眼.csv","a",newline="") as f:
    # 初始化写入对象
    writer = csv.writer(f)
    #把列表写入到文件中
    writer.writerow(["电影名称","主演"])
    writer.writerow(["霸王别姬","张国荣"])
    writer.writerow(["唐伯虎点秋香","周星驰"])











