#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ITsystem'
__mtime__ = '2015/10/30'

import time,uuid,threading
t=time.time()
print t
print '%015d%s000' % (int(t*1000),uuid.uuid4().hex)