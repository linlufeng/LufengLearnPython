#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
注意：通常你需要在单独的文件中定义一个类，
类的继承
面向对象的编程带来的主要好处之一是代码的重用，实现这种重用的方法之一是通过继承机制。
通过继承创建的新类称为子类或派生类，被继承的类称为基类、父类或超类。
继承语法
class 派生类名(基类名)
    ...
'''

'''
在python中继承中的一些特点：
1、如果在子类中需要父类的构造方法就需要显示的调用父类的构造方法，或者不重写父类的构造方法。详细说明可查看：python 子类继承父类构造函数说明。
2、在调用基类的方法时，需要加上基类的类名前缀，且需要带上 self 参数变量。区别在于类中调用普通函数时并不需要带上 self 参数
3、Python 总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。（先在本类中查找调用的方法，找不到才去基类中找）。
如果在继承元组中列了一个以上的类，那么它就被称作"多重继承" 。
语法：
派生类的声明，与他们的父类类似，继承的基类列表跟在类名之后，如下所示：
class SubClassName (ParentClass1[, ParentClass2, ...]):
    ...
'''

class Parent:   # 定义父类1
    parentAttr = 100
    def __init__(self):
        print "调用父类构造函数"
    def method(self):
        print "调用父类方法"
    def setAttr(self, attr):
        Parent.parentAttr = attr
    def getAttr(self):
        print "父类属性:", Parent.parentAttr

class Mother:   # 定义父类2
    motherAttr = 100
    def __init__(self):
        print "调用母亲构造函数"
    def method(self):
        print "调用母亲方法"
    def setAttr(self, attr):
        Mother.motherAttr = attr
    def getAttr(self):
        print "母亲属性:", Mother.motherAttr

class Child(Parent,Mother):    # 定义子类
    def __init__(self):
        print "调用子类构造方法"
    def childMethod(self):
        print "调用子类方法"

c = Child()             # 实例化子类
c.childMethod()         # 调用子类方法
c.method()              # 调用父类方法,多重继承时候,看哪个父类写在前面就调用哪个父类的方法
c.setAttr(200)          # 调用父类方法 - 设置属性值
c.getAttr()             # 调用父类方法 - 获取属性值
print issubclass(Child, Parent)
print isinstance(c, Child)

'''
你可以继承多个类
class A:        # 定义类 A
.....

class B:         # 定义类 B
.....

class C(A, B):   # 继承类 A 和 B
.....
你可以使用issubclass()或者isinstance()方法来检测。
issubclass() - 布尔函数判断一个类是另一个类的子类或者子孙类，语法：issubclass(sub,sup)
isinstance(obj, Class) 布尔函数如果obj是Class类的实例对象或者是一个Class子类的实例对象则返回true。
'''