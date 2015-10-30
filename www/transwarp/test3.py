#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ITsystem'
__mtime__ = '2015/10/30'

import time


def timeit(func):
    def wrapper():
        start = time.clock()
        func()
        end = time.clock()
        print 'used: ',end -start
    return wrapper

@timeit
def foo():
    print 'in foo()'



