# print('----------装饰器decorate练习----------')
### 1.不带参数的函数
# def endsign(func):
#     def wrapper():
#         return func()+'!!!'
#     return wrapper
# @endsign
# def hello():
#     return 'hello'
# # hello = endsign(hello)
# print(hello())

### 2.带参数的函数
# def endsign(func):
#     def wrapper(*args,**kwargs):
#         return func(*args,**kwargs) + '???'
#     return wrapper
# @endsign
# def hello(arg1, arg2=''):
#     return 'hello %s %s' % (arg1,arg2)
# # hello = endsign(hello)
# print(hello('cat',arg2='dog'))

### 3.带参数的装饰器
def endsign(tail):
    def inner(func):
        def wrapper():
            return func()+' '+tail
        return wrapper
    return inner
@endsign('@+@')
def hello():
    return 'hello'
# hello = endsign('@@')(hello)
print(hello())
