'''
    每个模块一般都要有一段说明    
'''
# user_name = 'hello'
# pass_word = 121212

# # snippet 片段

# if True:
#     print('hello python.')
# else:
#     pass

'''
    类、对象
    1.类最基本的作用：封装
    2.类下用self调用
    3.方法：设计层面。函数：程序运行、过程式的一种称谓。
    4.类就像一个模板一样，可以创建多个对象。
    python 类
        变量：类变量、实例变量
        方法：实例方法、类方法、静态方法
        构造函数
    5.类中定义的变量和方法，如果想实现私有的，使用双下划线前缀即可，__pri
    6.

'''
class Student():
    name='aa'
    age=10
    sum = 0
    # 行为 与 特征
    # 类变量(类中)、实例变量(对象中)
    # 构造函数
    # 实例方法 第一个参数为self
    # 类方法，函数前加上@classmethod，装饰器

    # self只和对象有关，代表的是实例对象
    def __init__(self,name1,age):
    # 构造函数，初始化对象的属性(特征)
        self.name = name1    # 实例变量赋值使用self.name
        self.age = age
        self.__score = 0    # 定义私有变量或者方法，双下划线在前 __
        # print(self.name)    # 打印实例变量
        # print('__init__中的传入的name值:' + name1) # 打印的是传入的形参

        # 实例方法中操作类变量
        # print(Student.sum1) # (方法1)，使用类名.类变量
        self.__class__.sum += 1
        print('班级总人数：' + str(self.__class__.sum))  # (方法2)

        # print('打印构造函数__init__')
        # return None #构造函数只能返回None

    # 实例方法，第一个参数要传入self
    def do_homework(self):
        print('do_homework..')
        self.do_english_hw()    # 实例方法的内部调用

        # self.__class__.sum += 1
        # print('班级总人数：' + str(self.__class__.sum))  # 在实例方法内部访问类变量(第二种方法)
        # print('name=' + self.name)
        # print('age=' + str(self.age))

    def do_english_hw(self):
        print('do_english_homework..')

    # 对类变量的修改应该使用方法来操作，不建议直接操作修改类变量，旨在保护数据
    def update_class_data(self,score):
        if score < 0:
            return print('打分值为负数，请重新打分！')
        self.__score = score
        print(self.name + '的分数为：' + str(self.__score))

    # 类方法，函数开头使用特殊标记 @classmethod，装饰器
    # 参数列表里第一个为cls，主要作用是操作的是类的一些变量
    @classmethod
    def class_sum(cls):
        cls.sum += 1
        print(cls.sum)

    # 静态方法，函数开头使用 @staticmethod，装饰器
    @staticmethod
    def add(x,y):
        print('x+y=', x+y)


stu = Student('jack1',11)    # 实例化对象时会执行构造函数中的语句
# Student.class_sum() # 调用类方法
# stu.class_sum() # 不建议使用对象调用类的方法
stu.do_homework()
stu.update_class_data(99)
print(stu.__dict__) # 使用__dict__查看对象的属性
stu.update_class_data(-1)
print(stu.__dict__)
# stu.add(1,2)
# Student.add(1,3)    # 静态方法可以同时被类和对象调用

# stu = Student('jack2',12)
# Student.class_sum()
# stu = Student('jack3',13)
# Student.class_sum()

# print(stu.name) # 程序访问实例变量顺序：先从对象中查找，在从类中找，最后从父类中查找
# print(Student.name)
# print(Student.sum)

# stu.do_homework()

