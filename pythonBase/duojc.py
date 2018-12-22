'''
    面向对象的3大特性：封装性、继承性、多态性

'''
class People():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def people_fun(self):
        print('我是父类，people.')

class Student(People):
    def __init__(self,name,age,school):
        self.school = school
        # People.__init__(self,name,age)  # 在子类里调用父类的构造函数
        super(Student,self).__init__(name,age)  # 使用super关键字调用父类构造函数

    def do_english_hw(self):
        print('我是子类，do_english_homework..')

    def people_fun(self):
        super(Student,self).people_fun()
        print('这是子类的people..')

stu = Student('jack1',11,'清华小学')    # 实例化对象时会执行构造函数中的语句
stu.do_english_hw()
stu.people_fun()
print(f"姓名：{stu.name},年龄：{stu.age},在{stu.school}上学")
