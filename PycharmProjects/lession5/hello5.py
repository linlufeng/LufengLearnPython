#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Python 获取某月日历

import calendar

cal = calendar.month(2018, 12)
print "以下输出2018年12月份的日历:"
print cal

print calendar.weekday(2018,12,5)
print calendar.calendar(2018,2)