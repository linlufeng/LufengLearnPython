#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Employee:

    def __init__(self, age):
        self.age = age
    def __cmp__(self, other):
        if self.age > other.age:
            return True
        else:
            return False

    def __str__(self):
        return "aaaa"

class Employer:
    def __init__(self, age):
        self.age = age

e1 = Employee(30)
e2 = Employer(40)
print cmp(e1, e2)
print str(e1)


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector(%d, %d)', self.a, self.b

    def __add__(self, other):
        return Vector(self.a+other.a, self.b+other.b)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print v1+v2

