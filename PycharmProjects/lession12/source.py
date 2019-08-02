#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time;

ticks = time.time()
print ticks

localtime = time.localtime(time.time())
print localtime

asctime = time.asctime(time.localtime(time.time()))
print asctime

print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
a = "Fri Jul 12 17:32:32 2019"
print time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))

print time.clock()

print time.altzone()