'''01_json.loads示例.py'''
import json

# json格式的数组
jsarray = '[1,2,3,4]'
# 数组 -> 列表
L = json.loads(jsarray)
print(type(L),L)

# json格式对象
jsobj = '{"city":"天地会","name":"步惊云"}'
# 对象 -> 字典
D = json.loads(jsobj)
print(type(D),D)














