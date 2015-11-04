#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ITsystem'
__mtime__ = '2015/11/4'

import threading,time

class MyThread(threading.Thread):
    def __init__(self,id):
        self.id=id
        super(MyThread,self).__init__()

    def run(self):
        # x=0
        time.sleep(10)
        print self.id

# if __name__=='__main__':
#     print time.ctime()
#     t1=MyThread(999)
#     t1.start()
#     t1.join()
#     for i in range(5):
#         print i
#     print time.ctime()

if __name__ == "__main__":
        t1=MyThread(999)
        t1.setDaemon(True)
        t1.start()
        # t1.join()
        print "I am the father thread."

