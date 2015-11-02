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
a={'abc':'cdb'}
b={'efv':'bug'}
# c=dict(names="b",doom='d')
c={}
for k,v in zip(a,b):
    c[k]=v
    print zip(a,b)
    print c[k]
# def test(names="abc",doom='def'):
#     c={}
#     for k,v in zip(names,doom):
#         c[k]=v
#         print 'the key is "%s" , the value is "%s"' % (k,c[k])
#
# a=test('ghjst','sfdgh')
# print a