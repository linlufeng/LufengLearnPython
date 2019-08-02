#!/usr/bin/python
# -*- coding: UTF-8 -*-


class A(object):
    bar = 1
    def func1(self):
        print "func1"

    @classmethod
    def func2(cls):
        print "func2"
        print cls.bar
        cls().func1()

A.func2()