#!/usr/bin/python
# -*- coding: UTF-8 -*-

print "Python 是一个非常棒的语言，不是吗？"

str = raw_input("please enter:")
print "your enter is : ", str


# input([prompt]) 函数和 raw_input([prompt]) 函数基本类似，但是 input 可以接收一个Python表达式作为输入，并将运算结果返回。
while True:
    content = input("please enter:")
    print "your enter is : ", content
