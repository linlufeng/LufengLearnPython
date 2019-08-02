#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Python continue 语句

myname = "linlufeng"
for c in myname:
    if c == 'l':
        continue
    else:
        print c

for letter in 'Python':  # 第一个实例
    if letter == 'h':
        continue
    print '当前字母 :', letter

var = 10  # 第二个实例
while var > 0:
    var = var - 1
    if var == 5:
        continue
    print '当前变量值 :', var
print "Good bye!"