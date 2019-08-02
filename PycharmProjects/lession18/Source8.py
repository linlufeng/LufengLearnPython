#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 描述
# type() 函数如果你只有第一个参数则返回对象的类型，三个参数返回新的类型对象。
# isinstance() 与 type() 区别：
# type() 不会认为子类是一种父类类型，不考虑继承关系。
# isinstance() 会认为子类是一种父类类型，考虑继承关系。
# 如果要判断两个类型是否相同推荐使用 isinstance()。

# 一个参数
print type(1)
print type("lufeng")
print type('lu')
print type(True)
print type([1, 2, 3,])
print type((1, 2, 3))

# 三个参数
class X(object):
    a = 1

Y = type('Y', (object,), dict(a=1))
print Y


class A(object):
    pass

class B(A):
    pass

print isinstance(A(), A)    # True
print type(A()) == A        # True
print isinstance(B(), A)    # True
print type(B()) == A        # False