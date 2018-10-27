print('-------线程练习------')
'''
1.进程 process，就是一段程序的执行过程。进程的三个状态：就绪、运行和阻塞
2.程序 是指令和数据的集合，其本身没有实际意义，是个静态的概念。
3.线程 thread，线程，是进程的一部分，一个没有线程的进程可以被看作是单线程的。
  线程有时又被称为轻权进程或轻量级进程，也是 CPU 调度的一个基本单位。
4.线程库
  thread(仅在Python2中有，Python3中已经没有)
  threading
  二者都可以用来创建和管理线程。
  thread比较底层；threading是thread的扩展，提供了很多线程同步功能，更加强大。
5.多线程，一个程序并行执行代码的能力
6.threading.Thread 只是创建线程对象
7.threading用于提供线程相关的操作，线程是应用程序中工作的最小单元。
8.threading模块提供的类：
  Thread, Lock, Rlock, Condition, [Bounded]Semaphore, Event, Timer, local。
9.threading 模块提供的常用方法： 
  threading.currentThread(): 返回当前的线程变量。 
  threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。 
  threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。
10.threading 模块提供的常量：
  threading.TIMEOUT_MAX 设置threading全局超时时间。

'''
## 1.线程
# import threading
# import time
#
# def threadWash(args):
#     print('start washing dishes..', time.strftime('%Y-%m-%d %H:%M:%S'))
#     time.sleep(args)
#     print('end washing dishes..', time.strftime('%Y-%m-%d %H:%M:%S'))
#
# def threadDry(args):
#     print('start drying dishes...', time.strftime('%Y-%m-%d %H:%M:%S'))
#     time.sleep(args)
#     print('end drying dishes...', time.strftime('%Y-%m-%d %H:%M:%S'))
#
# if __name__ == '__main__':
#     thread1 = threading.Thread(target=threadWash,args=(1,))
#     thread2 = threading.Thread(target=threadDry,args=(2,))
#     thread1.start()
#     thread2.start()
#     thread1.join()
#     thread2.join()

# 2.线程
import time
import threading

## 定义
def thread1(seconds):
    print('thread1 start at ',time.ctime())
    time.sleep(seconds)
    print('thread1 end at ',time.ctime())

def thread2(seconds):
    print('thread2 start at ',time.ctime())
    time.sleep(seconds)
    print('thread2 end at ',time.ctime())

print('Main thread start')
## 此时还没产生新的线程，只是创建线程对象
# args参数是线程入口函数的参数，参数必须放在一个元组里面，(5,)表示是一个元组
t1 = threading.Thread(target=thread1, args=(2,))
t2 = threading.Thread(target=thread2, args=(1,))
t1.start()      ## 此时才会创建一个新的线程
t2.start()
t1.join()       ## 当前执行join的线程需等待tt线程执行完成之后，在执行
t2.join()
# time.sleep(2)
print('Main thread end')


