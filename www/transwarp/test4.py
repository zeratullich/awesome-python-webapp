#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ITsystem'
__mtime__ = '2015/10/30'

def getTalk(type="shout") :

    # 我们定义另外一个函数
    def shout(word="yes") :
        return word.capitalize()+" !"

    def whisper(word="yes") :
        return word.lower()+"...";

    # 然后我们返回其中一个
    if type == "shout" :
        # 我们没有使用(),因为我们不是在调用该函数
        # 我们是在返回该函数
        return shout
    else :
        return whisper

# 然后怎么使用呢 ?

# 把该函数赋予某个变量
talk = getTalk()

# 这里你可以看到talk其实是一个函数对象:
print talk

# 该对象由函数返回的其中一个对象:
print talk()

# 或者你可以直接如下调用 :
print getTalk("whisper")()