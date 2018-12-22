# 时间回顾熟悉 #unix时间戳，定义为从格林威治时间1970-01-01 00:00:00起到现在的总秒数
# from time import time,strftime,localtime
# 1543629770.4794893 时间戳
# print(time.time())
# print(time.ctime())
# print(strftime("%Y-%m-%d %H:%M:%S",localtime()))

'''
    装饰器 - 无参数
    1.语法糖 @符号
    2.
'''
# import time

# def decorate(func):
#     def wrapper():
#         print(time.time())
#         func()
#     return wrapper

# @decorate
# def func_pri():
#     print('this is a function print.')

# func_pri()
# 等价于以下两行
# f1 = decorate(func_pri)
# f1()


'''
    装饰器 - 有参数
'''
import time

def decorate(func):
    def wrapper(*args, **kw):
        print(time.time())
        func(*args, **kw)
    return wrapper

@decorate
def func1(fun_name):
    print('this is a function, name is ' + fun_name + '.')

# *args 接收可变参数
@decorate
def func2(fun_name,fun_length):
    print(f'this is a function, name is {fun_name}, length is {fun_length}.')

# **kw 接收关键字参数 key word
@decorate
def func3(fun_name,fun_length,**members):
    print(f'this is a function, name is {fun_name}, length is {fun_length}.')
    print(members)

func1('test_fun')
func2('test_fun2',20)
func3('test_fun3',30,a=1,b=2,c='hello')
