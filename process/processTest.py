# print('------多进程process------')
# import random
# print(random.randint(1,5))
# print(list(range(0,5)))

'''
1.  创建子进程
    fork()系统调用,但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），
    然后，分别在父进程和子进程内返回。子进程永远返回0，而父进程返回子进程的ID。
'''
# import os
# print(f'process {os.getpid()} start...')
#
# pid = os.fork()
# if pid == 0:
#     print(f'this {os.getpid()} is child process, parent is {os.getppid()}')
# else:
#     print(f'i am parent {os.getpid()}, child is {pid}')

'''
2.  多进程 multiprocessing,跨平台的多进程
    multiprocessing模块提供了一个Process类来代表一个进程对象
'''
# from multiprocessing import Process
# import os
#
# def son_proc(args):
#     print(f'child process {os.getpid()},args={args}')
#
# if __name__ == '__main__':
#     print(f'parent process {os.getpid()}')
#     pson = Process(target=son_proc,args=('parameters',))
#     print('child process start...')
#     pson.start()
#     pson.join()     ## join()方法可以等待子进程结束后再继续往下运行
#     print('child process end...')

'''
3.  进程池 pool,如果要启动大量的子进程，可以用进程池的方式批量创建子进程
'''
# from multiprocessing import Pool
# import os,time,random
#
# def sub_proc(args):
#     print(f'sub task {os.getpid()},name = {args}')
#     time.sleep(random.random()*2)
#
# if __name__ == '__main__':
#     print(f'parent process is {os.getpid()}')
#     p = Pool(4)
#     for i in range(10):
#         p.apply_async(sub_proc, args=(i,))
#     p.close()
#     p.join()
#     print('all process done.')

'''
4.  进程间通信,Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据
    
'''
import os,time
from multiprocessing import Process,Queue

def sub_write(q):
    print(f'write process {os.getpid()}')
    for value in ['A','B','C','D']:
        print(f'put {value} into queue.')
        q.put(value)
        time.sleep(2)

def sub_read(q):
    print(f'read process {os.getpid()}')
    while True:
        print(f'get {q.get()} from queue.')

if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=sub_write, args=(q,))
    pr = Process(target=sub_read, args=(q,))
    # 启动子进程pw，写入
    pw.start()
    # 启动子进程pr，读取
    pr.start()
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止
    pr.terminate()
    print('queue process done......')


