#!/usr/bin/python
# -*- coding: UTF-8 -*-

class A(object):
    a = 1
    b = "b"

obj = A()
print hasattr(obj, 'a')
print hasattr(obj, 'b')
print hasattr(obj, 'c')

print hash(obj)

v = memoryview('abcd')
print v
print v[1]
print v[1:2]
print v[1:3].tobytes()


print round(3.1415, 1)  # 3.1
print round(3.1415, 3)  # 3.142

__import__('Source13')

print complex(1, 2)
print complex("1+2j")
print min(1, 3, 5, 0, 10)
print min(-10, -99, 100, 0, 5)