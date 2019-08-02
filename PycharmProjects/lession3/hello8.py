#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Python pass 语句
'''
Python pass是空语句，是为了保持程序结构的完整性。
pass 不做任何事情，一般用做占位语句。
'''

myname = "linlufeng"
for c in myname:
    if c == 'l':
        pass
        print "this is pass block"
    else:
        print c