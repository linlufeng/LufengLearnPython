#!/usr/bin/python
# -*- coding: UTF-8 -*-

class C(object):
    def __init__(self):
        self._x = None

    def getx(self):
        print "get"
        return self._x

    def setx(self, value):
        print "set"
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property")


    def __delete__(self, instance):
        print "hahaha"

c = C()
c.x = 1
