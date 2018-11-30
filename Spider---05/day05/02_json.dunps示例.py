'''02_json.dunps示例.py'''
import json

L = [1,2,3,4]
T = (1,2,3,4)
D = {"city":"天地会","name":"聂风"}
# python格式 -> json格式
jsarray1 = json.dumps(L)
print(type(jsarray1),jsarray1)

jsarray2 = json.dumps(T)
print(type(jsarray2),jsarray2)

jsobj = json.dumps(D,ensure_ascii=False)
print(type(jsobj),jsobj)











