#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ITsystem'
__mtime__ = '2015/11/3'

import threading
from time import ctime,sleep

def music(func):
    for i in range(2):
        print "I was listening to music %s. %s" %(func,ctime())
        sleep(6)
        print 'the music "%s" has end at %s' % (func,ctime())

def move(func):
    for i in range(2):
        print "I was at the movies %s! %s" %(func,ctime())
        sleep(4)
        # print 'the movie "%s" has end at %s!' %(func,ctime())

class MyThread(threading.Thread):
    def __init__(self,*arg,**kw):
        super(MyThread ,self).__init__(*arg,**kw)
        self.setName("new" +'-'+ self.name)

threads=[]
t1=MyThread(target=music,args=('K歌之王',))
t1.setName('线程1')
threads.append(t1)
t2=MyThread(target=move,args=('黑暗骑士',))
t2.setName('线程2')
threads.append(t2)
print threads
if __name__ == '__main__':
    # music('K歌之王')
    # move('黑暗骑士')
    print 'the main process is %s' % (threading.current_thread().name)
    for t in threads:
        t.setDaemon(True)
        t.start()
        # print t
    t.join()
    # t1.start()
    # t2.start()
    # t1.join()
    print t.name
    # t2.join()

    print "all over %s . the main process is %s" % (ctime(),threading.current_thread().name)




