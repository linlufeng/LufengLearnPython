#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Python 循环嵌套

i = 2
while (i < 100):
    j = 2
    while (j <= (i / j)):
        if not (i % j): break
        j = j + 1
    else: print i, " 是素数"
    i = i + 1

print "Good bye!"