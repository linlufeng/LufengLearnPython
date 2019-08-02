#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 打开和关闭文件
# 现在，您已经可以向标准输入和输出进行读写。现在，来看看怎么读写实际的数据文件。
# Python 提供了必要的函数和方法进行默认情况下的文件基本操作。你可以用 file 对象做大部分的文件操作。
# open 函数
# 你必须先用Python内置的open()函数打开一个文件，创建一个file对象，相关的方法才可以调用它进行读写。
# 语法：
# file object = open(file_name [, access_mode][, buffering])

# close()方法
# File 对象的 close（）方法刷新缓冲区里任何还没写入的信息，并关闭该文件，这之后便不能再进行写入。
# 当一个文件对象的引用被重新指定给另一个文件时，Python 会关闭之前的文件。用 close（）方法关闭文件是一个很好的习惯。
# 语法：
# fileObject.close()

# 打开一个文件
fo = open("foo.txt", "w")
print "文件名: ", fo.name
print "是否已关闭 : ", fo.closed
print "访问模式 : ", fo.mode
print "末尾是否强制加空格 : ", fo.softspace

# 写文件
fo.write( "www.runoob.com!\nVery good site!\n")

# 关闭打开的文件
fo.close()

# read()方法
# read（）方法从一个打开的文件中读取一个字符串。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字。
# 语法：
# fileObject.read([count])
# 在这里，被传递的参数是要从已打开文件中读取的字节计数。该方法从文件的开头开始读入，如果没有传入count，它会尝试尽可能多地读取更多的内容，很可能是直到文件的末尾。

# 打开一个文件
fo = open("foo.txt", "r+")
str = fo.read(10)
print "读取的字符串是 : ", str
# 关闭打开的文件
fo.write("\n"+str)
fo.close()