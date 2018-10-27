print('---线程共享资源，使用锁机制---')
'''
    当多个线程同时执行lock.acquire()时，
    只有一个线程能成功地获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止。
'''
import threading,time
lock = threading.Lock()     ## 创建一个锁就是通过threading.Lock()来实现

tempALL = {
    'account':10
}

def thread1(num):
    lock.acquire()      ## 先要获取锁
    global temp
    print('thread1 抢到资源执行...')
    time.sleep(1)
    temp = tempALL['account']
    tempALL['account'] = temp - num
    lock.release()      ## 最后释放锁

def thread2(num):
    lock.acquire()
    global temp
    print('thread2 抢到资源执行...')
    time.sleep(2)
    temp = tempALL['account']
    tempALL['account'] = temp + num
    lock.release()

if __name__ == '__main__':
    t1 = threading.Thread(target=thread1,args=(1,))
    t2 = threading.Thread(target=thread2,args=(5,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(temp)

'''
if __name__ == '__main__':
    解释：相当于Python模拟的程序入口，Python本身并没有这么规定，这只是一种编码习惯。
         当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；
         当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。
'''
