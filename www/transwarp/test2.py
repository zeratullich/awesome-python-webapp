#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ITsystem'
__mtime__ = '2015/10/29'

import time
def foo():
    print 'in foo()'

def timeit(func):
    start = time.clock()
    func()
    end = time.clock()
    print 'used: ',end - start

timeit(foo)


