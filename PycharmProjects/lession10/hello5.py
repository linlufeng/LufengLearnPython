#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
方法重写
如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法：
'''

class Parent:
    def myMethod(self):
        print 1+1

class Child(Parent):
    def myMethod(self):
        print 2+2
c = Child()
c.myMethod()
d = c
print repr(c)
print str(d)
print cmp(c,d)
'''
基础重载方法
下表列出了一些通用的功能，你可以在自己的类重写：
序号	方法, 描述 & 简单的调用
1	__init__ ( self [,args...] )
构造函数
简单的调用方法: obj = className(args)
2	__del__( self )
析构方法, 删除一个对象
简单的调用方法 : del obj
3	__repr__( self )
转化为供解释器读取的形式
简单的调用方法 : repr(obj)
4	__str__( self )
用于将值转化为适于人阅读的形式
简单的调用方法 : str(obj)
5	__cmp__ ( self, x )
对象比较
简单的调用方法 : cmp(obj, x)
'''

'''
运算符重载
Python同样支持运算符重载，实例如下：
'''
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Vector (%d, %d)' % (self.x, self.y)

    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y)
v1 = Vector(1,2)
v2 = Vector(3,4)
v3 = v1+v2
print v3
print str(v3)