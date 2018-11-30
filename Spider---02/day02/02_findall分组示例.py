import re
#解释 ：先按照整体匹配出来,然后再匹配()中的
# 如果有2个或者多个(),则以元组的方式取显示

s = "A B C D"
p1 = re.compile('\w+\s+\w+')
print(p1.findall(s))
# ['A B','C D']

p2 = re.compile('(\w+)\s+\w+')
# 第1步 ：['A B','C D']
# 第2步 ：['A','C']
print(p2.findall(s))

p3 = re.compile('(\w+)\s+(\w+)')
# 第1步 ：['A B','C D']
# 第2步 ：[('A','B'),('C','D')]
print(p3.findall(s))













