#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ITsystem'
__mtime__ = '2015/11/3'


import time, threading

# 新线程执行的代码:
def loop():
    print 'thread %s is running...' % threading.current_thread().name
    n = 0
    while n < 5:
        n = n + 1
        print 'thread %s >>> %s' % (threading.current_thread().name, n)
        time.sleep(1)
    print 'thread %s ended.' % threading.current_thread().name

print 'thread !! %s is running...' % threading.current_thread().name
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print 'thread ?? %s ended.' % threading.current_thread().name

import time, threading

# 假定这是你的银行存款:
balance = 0
lock = threading.Lock()
def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        lock.acquire()
        try:
             change_it(n)
        finally:
            lock.release()


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(10,))
t1.start()
t1.join()
t2.start()
t2.join()
print balance


# import threading, time, random
# count = 0
# class Counter(threading.Thread):
#     def __init__(self, lock, threadName):
#         '''@summary: 初始化对象。
#
#         @param lock: 琐对象。
#         @param threadName: 线程名称。
#         '''
#         super(Counter, self).__init__(name=threadName)  #注意：一定要显式的调用父类的初始化函数。
#         self.lock = lock
#
#     def run(self):
#         '''@summary: 重写父类run方法，在线程启动后执行该方法内的代码。
#         '''
#         global count
#         self.lock.acquire()
#         for i in xrange(10000):
#             count = count + 1
#         self.lock.release()
# lock = threading.Lock()
# for i in range(5):
#     Counter(lock, "thread-" + str(i)).start()
# time.sleep(2)	#确保线程都执行完毕
# print count
