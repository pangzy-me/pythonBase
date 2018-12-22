'''
    1.正则表达式 regular expression，
        是一个特殊的字符序列，检验一个字符串是否与所设定的字符序列相匹配
    2.json，需用""，双引号，是数据交换的一种标准格式。字符串是是json的表现形式。
    3.json对象、json、json字符串的理解：
      

'''
# a = 'hello,world'
# print(a.index('hello')>-1)  # 检验字符串中是否包含某字符
# print('hello' in a )
import json

str2json = '{"name":"xiaolan","age":18}'
# dict 反序列化：由字符串到某一种格式的过程叫反序列化。
stu = json.loads(str2json)
print(type(stu))
print(stu)

json2str = {"car":"BMW","color":"black"}
# str 序列化：由某一种格式到字符串的过程叫序列化
print(type(json2str))
stu2 = json.dumps(json2str)
print(type(stu2))
print(stu2)
