#!/usr/bin/python
# -*- coding: UTF-8 -*-

class JustCounter:
    __secretCount = 0
    publicCount = 0

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print self.__secretCount

counter = JustCounter()
counter.count()
counter.count()

print counter.publicCount
print counter._JustCounter__secretCount


class JJ(JustCounter):
    def __init__(self):
        print self.publicCount

jj = JJ()