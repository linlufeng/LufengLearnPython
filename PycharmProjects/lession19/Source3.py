#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
在python中继承中的一些特点：
1、如果在子类中需要父类的构造方法就需要显示的调用父类的构造方法，或者不重写父类的构造方法。详细说明可查看：python 子类继承父类构造函数说明。
2、在调用基类的方法时，需要加上基类的类名前缀，且需要带上 self 参数变量。区别在于类中调用普通函数时并不需要带上 self 参数
3、Python 总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。（先在本类中查找调用的方法，找不到才去基类中找）。
如果在继承元组中列了一个以上的类，那么它就被称作"多重继承"
'''


class Parent:
    parentAttr = 100
    def __init__(self):
        print "调用父类构造函数"

    def parentMetho(self):
        print "调用父类方法"

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print "父类属性", Parent.parentAttr

    def myPrint(self):
        print "Parent"


class Mother:
    def myPrint(self):
        print "Mother"

class Child(Parent, Mother):

    def __init__(self):
        print "调用子类构造方法"
    def childMethod(self):
        print "调用子类方法"
    def myPrint(self):
        print "Child"

child = Child()
child.childMethod();
child.parentMetho()
child.setAttr(10086)
child.myPrint()
print issubclass(Child, Mother)
print issubclass(Child, Parent)
child.myPrint()