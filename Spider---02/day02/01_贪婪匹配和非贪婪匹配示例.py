import re

s = """<div><p>仰天大笑出门去,我辈岂是蓬蒿人</div></p>
<div><p>床前明月光,疑是地上霜</div></p>"""
# 创建编译对象
# re.S作用 ：使 . 能够匹配 \n 在内的所有字符
# 贪婪匹配 : .*  
p = re.compile('<div><p>.*</div></p>',re.S)
#非贪婪匹配 : .*?
p = re.compile('<div><p>.*?</div></p>',re.S)
# 匹配字符串s
r = p.findall(s)
print(r)


#["<div><p>仰天大笑出门去,我辈岂是蓬蒿人</div></p>",
# "<div><p>床前明月光,疑是地上霜</div></p>"]







