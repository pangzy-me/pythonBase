
'''函数式编程'''

'''
1.    闭包
'''
# # 闭包 = 函数 + 环境变量
# # 由函数及定义时的环境变量(在函数外部，但非全局变量)所构成的一个整体，叫做闭包。
# def out_fun():
#     a = 10
#     def in_fun(x):
#         return a*x*x    # 在in_fun中没定义a，函数外有定义
#     return in_fun

# a = 20
# fun = out_fun() # 闭包 #函数调用时不会被变量重新赋值所影响
# print(fun(2))

'''
2.    匿名函数 lambda
'''
# def add(x,y):
#     return x+y

# f = add(2,3)
# print(f)

# # 匿名函数
# f2 = lambda x,y: x+y
# print(f2(1,2))

'''
3.    map 是一个类 class map(func, *iterables)
'''
# lista = [1,2,3,4,5]

# def square(x):
#     return x*x

# r = map(square,lista)   # 调用map会把集合中的元素传入到square中，并接受函数返回结果
# print(list(r))

'''
    map 和 匿名函数lamdba结合 # lamdba代替了上述定义的square()函数
    1.如果lambda表达式传入了两个参数，需传入两个列表，需同参数个数保持一致
    2.通过map计算的结果列表中的元素个数取决于两个集合中最少的个数
'''
# listb = [1,2,3,4,5]
# listc = [1,2,3,4,5,6,7,8]
# rb = map(lambda x,y: x*x + y, listb, listc)
# print(list(rb))

'''
4.    reduce 是一个函数 def reduce(function, sequence, initial)
'''
# from functools import reduce

# # 连续计算，连续调用lambda，执行过程理解 (((((1+2)+3)+4)+5)+6)
# listc = ['1','2','3','4','5','6']
# rc = reduce(lambda x,y: x+y, listc, 'aaa')
# print(rc)

# 大数据里的map/reduce 是一种编程模型 映射 归约 并行计算

'''
5.  filter 过滤器，是一个类 class filter(function or None, iterable)
'''
listd = [1,0,1,0,1]
rd = filter(lambda x : True if x == 1 else False, listd)
print(list(rd))


'''
    函数式编程      #python语言支持函数式编程
    map reduce filter
    lambda 算子
&   
    命令式编程
    def
    if else
    for
'''
