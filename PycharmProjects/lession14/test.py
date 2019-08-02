#!/usr/bin/python
# -*- coding: UTF-8 -*-

import support
from fib import sub
from lib import  *
support.print_func("linlufeng")

print support.add(10,5)

sub(100, 1)

aa()

bb()

money = 2019

def addMoney():
    global money
    money = money + 1

print money
addMoney()
print money

print dir(support)