#!/usr/bin/python
# -*- coding: UTF-8 -*-

x = set("linlufeng")
y = set("linjunjie")
print x - y # 差 set(['g', 'f'])
print x & y # 交 set(['i', 'u', 'e', 'l', 'n'])
print x | y # 并 set(['e', 'g', 'f', 'i', 'j', 'l', 'n', 'u'])

class A(object):
    a = 1
    b = 'b'
    c = 1.0

obj = A()
delattr(A, 'a')
obj.a