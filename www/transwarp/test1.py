#!/usr/bin/env python
#coding=utf-8
'''
__title__ = ''
__author__ = 'ITsystem'
__mtime__ = '2015/10/27'
'''
a=set('lichuanchou2')
b=set(['h','u','o','l','e'])
print a,b
print a-b
print a&b
print a|b


c= [i for i in a | b ]
print c

d=list(a)
print d

print '----------------'
fza=frozenset('a')
adict={fza:1,'b':2} #正确
print adict
setb=set('a')
bdict={setb:1,'b':2}
print bdict
