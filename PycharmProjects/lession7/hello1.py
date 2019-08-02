#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Python 文件I/O
# 本章只讲述所有基本的的I/O函数，更多函数请参考Python标准文档。

# 打印到屏幕
# 最简单的输出方法是用print语句，你可以给它传递零个或多个用逗号隔开的表达式。此函数把你传递的表达式转换成一个字符串表达式，并将结果写到标准输出如下：
print "Python 是一个非常棒的语言，不是吗？"

# 读取键盘输入
# Python提供了两个内置函数从标准输入读入一行文本，默认的标准输入是键盘。如下：
# raw_input
# input

# raw_input函数
# raw_input([prompt]) 函数从标准输入读取一个行，并返回一个字符串（去掉结尾的换行符）：

str = raw_input("please input content:")
print "你输入的内容是: ", str

# input函数
# input([prompt]) 函数和 raw_input([prompt]) 函数基本类似，但是 input 可以接收一个Python表达式作为输入，并将运算结果返回。
# [x*5 for x in range(2,10,2)]
str2 = input("please write:")
print "your write content is:", str2