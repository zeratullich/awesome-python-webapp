#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ITsystem'
__mtime__ = '2015/10/30'



def my_shiny_new_decorator(a_function_to_decorate) :
    def the_wrapper_around_the_original_function() :
        print "Before the function runs"
        a_function_to_decorate()
        print "After the function runs"
    return the_wrapper_around_the_original_function

def bread(func) :
    def wrapper() :
        print "</''''''\>"
        func()
        print "<\______/>"
    return wrapper

def ingredients(func) :
    def wrapper() :
        print "#tomatoes#"
        func()
        print "~salad~"
    return wrapper

@bread
@ingredients
def sandwich(food="--ham--") :
    print food

sandwich()

print  '-------------------------------------'

import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def wrapper():
        start = time.clock()
        func()
        end =time.clock()
        print 'used:', end - start
    return wrapper

@timeit
def foo():
    print 'in foo()'

foo()
print foo.__name__

print '---------------------'

def deco_functionNeedDoc(func):
    if func.__doc__ == None :
        print func, "has no __doc__, it's a bad habit."
    else:
        print func, ':', func.__doc__, '.'
    return func


@deco_functionNeedDoc
def f():
    print 'f() Do something'


@deco_functionNeedDoc
def g():
    '''I have a __doc__'''
    print 'g() Do something'

f()
g()
import  functools

print '-------------------------'
def log(text):
    if callable(text):
        @functools.wraps(text)
        def wrapper(*args, **kw):
            print 'begin call: ' + text.__name__
            text(*args, **kw)
            print 'end call: ' + text.__name__
        return wrapper
    else:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print 'begin call: '+text
                func(*args, **kw)
                print 'end call: '+text
            return wrapper
        return decorator

@log('testone!')
def f1(x,y):
    print x+y

@log
def f2(x,y):
    print x+y

f1(1,3)
print '++++++++++++++++'
f2(1,2)



