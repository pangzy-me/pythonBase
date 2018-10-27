# 2018-07-24
# # 注释/取消注释 ctrl + /
# print('hello world.')
# print("hello world!")
# help(print)
# # 一切数据皆为对象！
# # 查看类型 type
# print(type(200))
# print(9/4)  # 保留小数
# print(9//4) # 取整
# print(id(3))    # 打印 3 在堆内存的地址
# welcome = 'hello world.'
# print('a '+welcome)
# print('b '+welcome)
# # 保留关键字
# import keyword
# print(keyword.kwlist)
# # # 对于字符串中需要' 或者" 的，要么转义\，要么单双引号混用
# print("this is 'bbb")
# print('this is \'aaa')
# # 三单引号，一个是注释，一个是多行定义字符串
'''
注释语句，三引号
'''
# print('''name
# is
# tom
# ''')
# # 字符串重复多次
# print('hello\n' * 3)

# # sequence 序列部分
# str ='hello world'
# print(len(str))
# print(str[0])
# print(str[-1])
# print('a'+'b'+'c'+'ddddd')
# # ## 切片操作 slice ，字符串本身不变，左边包含右边不包含
# # ## 左边固定长度从左边切，右边固定长度从右边切
# str = 'abcde'
# ## 切两刀
# # print(str[2:2+2])
# # print(str[-3:-3+2])
# ## 切一刀
# print(str[2:])  # 左边切
# print(str[:3])  # 右边切

## 列表 sequence
'''
列表中元素可以改变值
'''
# list1=['a','b',45,66,3.1222]
# print(list1)
# list2=list1[2:2+2]
# print(list2)
# print('a' in list1)
# list1[2]=100
# print(list1)
# print(list2)

## 元组 tuple
'''
元组中元素不可以改变值
'''
# tup1=(3,'a',444.44,[1,2,3],'汉字',(5,6)) # 元素和值不可变
# print(tup1[5])
# print(tup1[3])
# ## 元组转列表，列表转元组。list,tuple
# list3=list(tup1)
# print(list3)    # 列表
# print(tup1)     # 元组
# list3.append(9)
# print(list3)
# list3.remove(444.44)
# print(list3)
'''
列表和元组的区别：
列表：可变，index，切片，[1]一个元素
元组：不可变，index，切片，(1，)一个元素
'''
## and or not
# print(3>1)
# print('a' in 'abc')
# print('a' in 'bbb')
# lista =[2,3,4,5]
# print(3 in lista)
## python 中没有switch，只能用if...elif...elif...来实现
# score=90
# if score>=80 and score<90:
#     print('分数合格！')
# elif score>=90:
#     print('分数优秀！')
# else:
#     print('不合格。。。')
# print('that is all.')
'''
函数
1.先定义后调用

'''

## 函数没有返回值时，返回的是None
# def fun1():
#     print('aaaa')
# print(fun1())
# print(type(fun1)) ## 查看对象类型
# def sumFun(a,b):
#     return a+b
#     print('程序执行完毕。')    # return后边的语句不执行
# print(sumFun(1,2))
## print(1,b=3)
## print(a=2,3) ##变量赋值可以在后，但是不能前赋值后不赋值。
# a=1
# def fun():
#     a=3
#     print('a=',a+2)
#     return a+2
# print('a的值为',a)
# print('a的内部值',fun())
# num = input('输入一个数值：')  # input 返回值为str
# print(int(num)+5)
'''
对象的方法
'''
# str1='abcdddd,bbb'
# print(str1.find('n'))   #返回元素的下标，没有的元素返回值为-1
# print(str1.count('d'))  #记数该字符出现的次数
# print(str1.startswith('ba'))
# print(str1.endswith('ddd'))
# print(str1.find('b',5))     #从index=5的地方开始往后找'b'的下标位置

# def checkTel():
#     while 1:
#         num=input('请输入手机号码：')
#         if(len(num)==11):
#             if(num.isdigit()):
#                 if(num.startswith('187') or num.startswith('188')):
#                     print('yidong user.')
#                 elif(num.startswith('134') or num.startswith('135')):
#                     print('liantong user.')
#                 elif(num.startswith('180') or num.startswith('181')):
#                     print('dianxin user.')
#                 else:
#                     print('hao ma duan shu you wu')
#             else:
#                 print('han you fei fa zifu.')
#         else:
#             print('hao ma you wu.')
#             exit()
# checkTel()

# stra ='aaa bbb ccc'
# print(stra.split(' '))  #切点 返回的是一个列表list
# print(stra.split('b'))  #切点，会被切去
# log='  ***2018-07-31***  '
# print(log.split('*')[3])
# print(log.replace('*','@')) # 替换
# print(log.strip())      # 去除左右空格
# print(log.lstrip())     # 去除左边空格
# print(log.rstrip())     # 去除右边空格
'''
list:
1. append 从后边增加
2. insert 指定位置插入一个元素
3. del 删除一个具体的值
4. pop 删除元素的同时，会得到元素的值
5. remove 删除元素的值，但是只能删除第一个匹配的值，最慢，遍历找
6. reverse 倒序（不是排序）
'''
# lista=[1,22,3,4,'a']
# lista.append('6')
# print(lista)
# lista.insert(3,'b')
# print(lista)
# del lista[3]
# print(lista)
# data=lista.pop(0)
# print(data)
# lista.remove(2)
# print(lista)
# lista.reverse()
# print(lista)

# 字符串拼接必须为字符串的，格式化输出
# s%,d%,f%,x%
# print('name is '+'tom,'+'age is '+str(16))
# name='tom'
# age=170
# print('name is %s, age is %dcm' % (name,age))
# ## 打印日志信息，可以考虑定义个变量使用
# plog='name is %s, age is %dcm' % (name,age)
# print(plog)
# print('%10d' % 333)     #右对齐-左补齐
# print('%5d' % 123456)   #全部输出
# print('%-10d' % 333)
# print('%f' % 3.1234567) #默认输出6位小数，多的四舍五入
# print('%.8f' % 3.123456789)
# print('%6.2f' % 33.12345)   #小数点也算1位
# print('%06.2f' % 33.12345)
'''
format:
1.顺序填坑
2.下标填坑
3.变量填坑
'''
# out='name is {}, age is {}'
# print(out.format('tom',18))
# outa='name is {1}, age is {0}'
# print(outa.format('heo',18))
# outaa='name is {name}, age is {age}'
# print(outaa.format(name='jack',age=12))
'''
数字、字符串对齐规则不同。可考虑不使用默认，使用 > 或者 < ，完成对齐。
'''
# print('{:10}'.format(56))   #默认右对齐
# print('{:>10}'.format(56))  # > 大于号，尖尖右对齐
# print('{:<10}'.format(56))  # < 小于号，尖尖左对齐
# print('{:10}'.format('hello'))   # 字符串，默认左对齐
# print('{:>10}'.format('hello'))  # > 大于号，尖尖右对齐
# print('{:<10}'.format('hello'))  # < 小于号，尖尖左对齐
# print('{:^10}'.format('hell'))    # 中间对齐
# print('{:*^10}'.format('jack'))
'''
格式化简单使用 f
'''
# name='haha'
# age=22
# print(f'name is {name}')
# print(f'name is {name},\nage is {age}.')
'''
取消转义字符 \    使用在文件路径中
1.使用两个\
2.使用 r
'''
# print('hello is \n a hello.')
# print('hello is \\n a hello.')
# print(r'hello is \n a hello...')
'''
input 返回的是str类型
'''
# data=input('input a data:\n')
# print(data)
# print(type(data))
'''
循环与注释   ## 注意：选择范围是左包含右不包含
1. while
2. for  遍历
  从list、tuple里获取每个元素进行处理
  break 跳出本层循环，之后的不在循环
  continue 跳过本次循环，之后的继续循环
'''
# while True:
#     str=input('请输入退出字母：')
#     if str=='q':
#         break
#
# i=0
# sum=0
# while i <101:
#     sum +=i
#     i += 1
# print(sum)
#
# sum=0
# for one in range(0,101):
#     sum += one
# print(sum)
#
# lista = ['aaa','bbb','ccc','ddd']
# for name in lista:
#     if name == 'bbb':
#         continue
#     print(name)
## 程序注释
# def fun():
#     'this is fun doc.'
#     pass
# print(fun.__doc__)
'''
文件读写：
1.文件的打开
2.文件的读
3.文件的写
4.with open('path') as filename  调用之后可以省略fopen.close()关闭文件
5.with open('path') as filename, open('path') as filename ## 打开多个文件
tell 方法获取文件指针
seek 
readline 读取一行
r+ w+ a+
'''
# fname = r'd:\python_pro\autoTest01\pythonBase\pythonFile.txt'
# fopen = open(fname, 'r')  ## 读文件
# print(fopen)
# print(fopen.read())
# fopen = open(fname, 'w')  ## 写文件
# fopen.write('aaa')
# fopen = open(fname,'a')
# fopen.write('\nbbb')
# fopen.flush()

# print('开始读取文件时文件指针的位置：', fopen.tell())
# print(fopen.read(2))    #有参数表示读取文件的长度，如果没有参数读取全部内容

# print(fopen.readline()) # 读取一行
# print(fopen.readlines()) # 读取所有行，返回一个列表 ['aaaaaaa\n', 'bbbbbbbbb\n']
# print('结束读取文件时文件指针的位置：',fopen.tell())
# readlines 读取的是包含'\n' ，可使用以下方法去除\n
# print('移动文件指针的位置到：',fopen.seek(0))
# print(fopen.read().splitlines())
# fopen.close()
# print(fopen.tell())
# fopen.seek(0)   # 移动文件指针位置，类似于下标
# print(fopen.tell())
'''
循环嵌套:
冒泡算法简单使用
函数应该先定义，后使用
'''
# lista=['aaa','bbb','ccc']
# listb=[11,22,33]
# for name in lista:
#     for age in listb:
#         print('name is %s, age is %d.' % (name,age))
# lista=[1,3,9,4,2,-1,5,0,100,50,99]
# # lista.sort() ## 排序
# # lista.sort(reverse= False) ## True 为降序，False 为升序
# for i in range(0,len(lista)-1):
#     for j in range(0,len(lista)-1-i):
#         if lista[j]>lista[j+1]:
#             tmp = lista[j + 1]
#             lista[j + 1] = lista[j]
#             lista[j] = tmp
# ## 或者使用: lista[j+1],lista[j] = lista[j],lista[j+1]
# print(lista)
'''
字典 dict 
列表是[],元组是(),字符串是''
列表和字典可以改变元素。其他的不行。
1.定义{} -- 键值对 key-value
2.字典不需要下标，是map映射
3.键值唯一
4.查询 dict['键']
5.增加字典元素，dict['key']=value
7.字典的键一定是不可改变的类型，list不行，不是hash类型。(字典、列表不能作为键名，可变的)
6.字典的值可以是任意类型
7.判断键在不在dict中 --'键名' in dict
8.字典删除元素，del，直接操作键名
9.字典遍历
10.清空字典 dicta.clear()  // dicta={}
11.字典不能排序，是无序的，是靠键去找的值
'''
## 列表可以增加删除元素
# lista=['aaa','bbb','ccc']
# lista.insert(1,'ddd')
# lista.append('eee')
# print(lista[1],lista[-1])
# dicta={'aa':34,'bb':'adb','cc':['a','b'],'dd':(34,'haha')}
# print(dicta['dd'])
# dicta['ee']=('hello')
# print(dicta)
# dicta['ee']=('hahalo')
# print(dicta)
# print('aa' in dicta)
# print(34 in dicta)
# del dicta['ee']
# print(dicta)
# print(dicta.keys()) ##输出所有键
# print(dicta.values()) ##输出所有值
# print(dicta.items()) ##输出所有键值
## 第一种方式打印所有键值
# for one in dicta:
#     print(one)  ##遍历键名
#     print(dicta[one])   ##遍历相应的键值
## 第二种方式打印所有键值
# print(dicta.items()) ##items 键值对的输出，列表list格式输出
# for jian,zhi in dicta.items():
#     print(jian)
#     print(zhi)
# print(len(dicta))
# dictb={'aa':34}
# print(dictb)
# dictb.clear()
# print(dictb)
'''
全局变量、局部变量
global a --局部变量转变为全局变量
fun(a,b) --a,b 为必填参数，缺一不可
fun(a,b,c=0) --c为可缺省参数，调用时c可不给值。但是缺省参数必须在必填参数后边

1.可变数量参数：在调用函数时，可输入任意个数的参数，传入的是一个元组 tuple
    a.def element(*nums):
    b.element(*lista))  -- *可以展开列表元素
2.关键字可变参数： **kw --字典(键:值)
    a.有关键字
    b.可变数量
    c.传入参数本身就是一个字典时， **dicta 展开字典，传入参数
## 综合使用： def fun(必填参数,可缺省,可变数量,关键字可变数量):
    可变数量与关键字可变数量的分界线：
        变量名=值 (此种情况为关键字可变数量)
'''
# 1.可变数量参数
# def element(*nums):
#     print(type(nums))   ## 查看传递参数的类型 --元组
#     sum=0
#     for i in nums:
#         sum += i*i
#     return sum
# # print(element(1,2,3))
# lista=[1,2,3]
# print(element(*lista))  ## *可以展开列表元素
# 2.关键字可变参数
# def keyWords(a,b,c=0,*nums,**kw):
#     print(type(nums))
#     print(type(kw))
#     print(a,b,c,nums,kw)
# # print(keyWords(1,2,3,4,5))
# # print(keyWords(1,2,3,4,5,name='jack',age=11))
# dicta={'call':'hello','sex':'male'}     ##推荐此种方式
# keyWords(1,2,3,4,5,**dicta)
'''
模块与包：
1. import 模块名
    1- 包内调用：
        函数调用：   模块名.函数()；
        变量调用：   模块名.变量
    2- 其他包调用：
        先导入该包：  包.子包.模块
        在找对应的模块
    3- 取别名：
        import 包.模块  as  selfName
2. from  模块名  import  函数，变量，类
    1- 调用： 函数()，变量
3. as
    1- 节省字符
    2- 避免不同模块之间的函数同名混淆，引用时覆盖

'''
# import sys
# print(sys.path)
'''
pyCharm使用技巧：
1. 调用函数处，ctrl + 左键单击查看函数
2. 定义函数处，ctrl + 左键查看调用函数的地方 / 右键点击"find Usages"
3. ctrl+alt+左箭头 返回上一步操
4. ctrl+alt+右箭头 返回下一步操作
5. 查找 ctrl+f、ctrl+shift+f(容易与搜狗输入法的简繁输入法切换快捷键冲突)
6. ctrl+g 查找行号
7. 显示历史版本 点击文件右键-> Local History -> show History
   可以在历史对比版本中 Revert 恢复代码
8. 重命名函数：在函数定义处，右键选择Refactor -> Rename...
   添加或者删除函数参数：在函数定义处，右键选择Refactor -> Change Signature...
9. 工程颜色是浅蓝色，表示根目录
   方法：选择工程，右键，Mark directory as...-> sources Root / Unmark as Sources Root
   import sys
   print(sys.path)
10.
'''
# print('--------debug--------')
'''
调试
方法一：断点+跟踪
1.行号后边单击即是加断点
2.
方法二：打印信息
1.

'''
# a=[1,2,3,4,5]
# b=[11,22,33,44,55]
# for i in a:
#     for j in b:
#         print('a=%d, b=%d ' %(i,j))
# print('all run over.')
## pprint 函数
# from pprint import pprint
# dict={"aa":"11212222221","bb":"222","cc":"333","dd":"11212222221","ee":"222",
#       "ff":"333","gg":"11212222221","qq":"222","ww":"333"}
# print(dict)     # 无排序输出，键值对数值较多时打印的数据格式凌乱
# pprint(dict)    # 键值对输出，美观易读
'''
面向对象1：类和对象
>>设计游戏<<
1.老虎
    属性：体重
    方法：吃、叫、睡、跑
2.羊：
    属性：体重
    方法：吃、叫、睡、跑
3.房间：
    属性：编号
         里面有动物(具体的对象)

1.
def __init__(self): ### 初始化方法，即构造方法
作用：只要创建实例，就会被调用
2.实例方法--有self的都叫实例方法。
def tell(self): ## 是具体的调用实例
作用：每个实例个体都有自己的输出
3.静态方法，也叫类方法，与每个具体实例无关
  @staticmethod 修饰，没有self

'''
# print('------class&object test------')
## 类首字母大写，不继承的话，不用加小括号();继承时加小括号()
class Tiger:
    ### 定义类属性(静态属性)，也叫类变量
    tigName="名字是老虎"
    ### 定义实例属性 --weight
    def __init__(self,weight=200):
        # print('初始化方法，一旦实例时，准会调用！')
        self.weight = weight
    ##实例方法
    def roar(self):
        print('WAWO!!!')
        self.weight -= 5
    def eat(self,food):
        if food == '肉':
            print('你喂对了。')
            self.weight += 10
        else:
            print('我是老虎，你喂错了。')
            self.weight -= 10

    ## self --实例方法
    # def eat(self):
    #     print('吃。。。')
    #
    # def tell(self): ## 是具体的调用实例
    #     print('体重是 %s.' % self.weight)
    #
    # @staticmethod ## 下面的方法为静态方法
    # def roar():
    #     print('WAWO!')

class Sheep:
    ##实例方法
    def roar(self):
        print('miemie....')
        self.weight -= 5
    def eat(self,food):
        if food == '草':
            print('你喂对了。')
            self.weight += 10
        else:
            print('我是小羊，你喂错了。')
            self.weight -= 10

class Room:
    def __init__(self,num,animal):
        self.num = num
        self.animal = animal

room1 = Room(1,Tiger(300))
# print(room1)

## 取随机数
# from random import randint
# print(randint(0,10)) ##闭区间，两端都可以取到数值
# ## 取时间
# import time
# print(time.time())

'''
继承
1.单继承
2.多继承
3.方法的重写
4.私有属性，私有方法。在类中用__xxx 表示
'''
class NiuTiger:
    niuTigerName = '最牛逼的老虎名字！'
    __name ='__私有属性'
    def __tell(self):
        print('__私有方法')

class SouthTiger(Tiger,NiuTiger): ## 括号内就是继承的父类
    ## 子类初始化方法里面，需要调用父类的初始化方法
    def __init__(self,weight):
        Tiger.__init__(self,weight)
    def roar(self):
        print('WAWOWAWOWAWO!!!')

# st= SouthTiger(500)
# print(st.tigName)
# print(st.niuTigerName)
# st.roar()   ## 子类的重写
# super(SouthTiger,st).roar() ## 使用super调用父类的方法

'''
异常
1.try...except...
对于未知异常的捕获：
方法一
2.1 Exception 指所有异常的父类，不清楚是哪种异常时使用，捕获所有异常。
    except Exception as e
        print ('抛出所有不明确的异常，捕获异常：', e)
方法二
2.2 import traceback
    except:
        print(traceback.format_exc())
3. else:
        没有异常的时候执行
4. finally:
        不管前面是否有异常，此异常肯定会执行！
5. raise ## 通过raise显示的引发异常，一旦执行raise语句，raise后边的语句将不能执行
   raise 可以实现异常逐层往上抛出
   举例：
    def fun1():
        raise
    def fun2():
        fun1()
        print('处理fun1抛过来的异常！')
6. 自定义异常，要继承父类Exception  ##待验证

'''
import traceback
class TextIncludeLetters(Exception):
    pass

while True:
    numa = 1000
    num = input('请输入一个除数：')
    try:
        # name
        print('numa/num=%d' % (numa/int(num)))
    except ZeroDivisionError:
        print('请再次输入除数不为0的数')
    # 方法一
    except Exception as e:
        print('抛出所有不明确的异常，捕获异常：\n', e)
        raise ## 捕获异常之后，抛出异常
    # 方法二
    # except:
    #     print(traceback.format_exc())
    # except TextIncludeLetters:
    #     print('除数包含字母，请重新输入：')
    else:   ### 可选项的输出
        print('No exception!!!')
    finally:
        print('一定会执行的异常！')
