'''
    枚举类 enum
    1.枚举类型的标签不能更改
'''

from enum import Enum
from enum import IntEnum,unique # 引入unique，装饰器，是为了防止枚举的值不重复
# IntEnum 枚举的值只能是数字；Enum的值可以为数字或者字符串

@unique
class VIP(IntEnum):
    BLACK = 1
    BLACK2 = 2
    WHITE = 0

# 枚举类型、枚举的名字、枚举的值
# print(VIP.BLACK)    # VIP.BLACK 枚举类返回的数据
# print(VIP.BLACK.name)  # 获取枚举类中标签的名字
# print(VIP.BLACK.value)  # 获取枚举类中标签对应的值
# print(VIP.BLACK == VIP.WHITE)   # 枚举中的比较操作
# print(VIP.BLACK is VIP.BLACK)   # 枚举中的比较操作

# 转换为枚举类型
a = 1 
print(VIP(a))

# # 数值相等时，第2个枚举标签不会被打印，只打印第一个。第二个被认为是第一个的别名
# for v in VIP:
#     print(v)

# # 使用此方法遍历所有标签，包括重复值的标签
# for v in VIP.__members__:   
#     print(v)

# # 使用此方法遍历所有标签和标签所对应的值
# for v in VIP.__members__.items():   
#     print(v)

# VIP.BLACK = 3 # 此时赋值会报错，枚举类不能更改值

