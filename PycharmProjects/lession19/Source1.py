#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Animal:
    '动物基类'
    def eat(self):
        print "eat"

class Dog(Animal):
    pass

dog = Dog()
dog.eat()


class Employee(object):
    '所有员工基类'

    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "员工数量为:", Employee.empCount

    def dispalyEmployeeInfo(self):
        print "Name : ", self.name, "salary : ", self.salary

    def prt(self):
        print self
        print id(self.__class__)
        print id(Employee.empCount)

ep1 = Employee("lin", 1)
ep2 = Employee("lu", 2)
ep3 = Employee("feng", 1)

ep1.displayCount()
ep1.dispalyEmployeeInfo()
ep1.prt()
ep2.prt()

ep1.age = 30
print ep1.age
del ep1.age

print hasattr(ep1, 'age')
print getattr(ep1, 'name')
setattr(ep2, 'age', 18)
print getattr(ep2, 'age')

print Employee.__dict__
print Employee.__name__
print Employee.__module__
print Employee.__bases__