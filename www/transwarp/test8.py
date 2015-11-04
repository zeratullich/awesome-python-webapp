#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ITsystem'
__mtime__ = '2015/11/3'

# class Student(object):
#
#     @property
#     def score(self):
#         return self._x
#
#     @score.setter
#     def score(self,value):
#         if not isinstance(value,int):
#             raise ValueError('MUST BE INTEGER!!')
#         if value < 0 or value > 100:
#             raise ValueError('SCORE MUST BETWEEN 0~100 !!')
#         self._x=value
#
#
# if __name__=='__main__':
#     s = Student()
#     s.score=699
#     print s.score

# class Parrot(object):
#     def __init__(self):
#         self._voltage = 100000
#
#     @property
#     def voltage(self):
#         """Get the current voltage."""
#         return self._voltage
#
# if __name__ == "__main__":
#     # instance
#     p = Parrot()
#     # similarly invoke "getter" via @property
#     print p.voltage
#     # update, similarly invoke "setter"
#     p.voltage = 12

class Parrot:
    def __init__(self):
        self._voltage = 100000

    @property
    def voltage(self):
        """Get the current voltage."""
        return self._voltage

if __name__ == "__main__":
    # instance
    p = Parrot()
    # similarly invoke "getter" via @property
    print p.voltage
    # update, similarly invoke "setter"
    p.voltage = 12
