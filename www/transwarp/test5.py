#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ITsystem'
__mtime__ = '2015/11/2'

import uuid

a=uuid.uuid1()
b=uuid.uuid3(uuid.NAMESPACE_DNS,'chuan.li')
c=uuid.uuid4()
d=uuid.uuid5(uuid.NAMESPACE_URL,'chuan.li')

print a
print b
print c
print d
a=(1,2,3)
b=(3,4,5)
c={}
for k,v in zip(a,b):
    c[k]=v
    print zip(a,b)
    print c[k]
e=dict(a='v',g='h')
print e

print dict(zip(('one', 'two'), (1, 2)))
print dict([('one', 1), ('two', 2), ('three', 3)])