#!/usr/bin/python
# -*- coding: UTF-8 -*-

l = [1, 2, 3, 4]
tp = tuple(l)
print tp
print list(tp)

print bool(-1)
print bool(0)
print bool(1)
print bool(2)

print issubclass(bool, int)


def fuc(n):
    if n % 2 == 0:
        return True
    else:
        return False

newlist = filter(fuc, l)
print newlist


name = "linlufeng"
print len(name)

