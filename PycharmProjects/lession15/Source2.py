#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
# 打开一个文件
fo = open("foo.txt", "a+")
flag = True

while flag:
    str = raw_input("enter:")
    if str == 'q':
        break
    else:
        fo.write(str)
fo.close()

print "文件名: ", fo.name
print "是否已关闭 : ", fo.closed
print "访问模式 : ", fo.mode
print "末尾是否强制加空格 : ", fo.softspace

# read()方法
# read（）方法从一个打开的文件中读取一个字符串。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字。
fo = open("foo.txt", "r+")
str = fo.read(5)
print "读到的字符串是：", str
fo.close()


# 文件定位
# tell()方法告诉你文件内的当前位置, 换句话说，下一次的读写会发生在文件开头这么多字节之后。
# seek（offset [,from]）方法改变当前文件的位置。Offset变量表示要移动的字节数。From变量指定开始移动字节的参考位置。
# 如果from被设为0，这意味着将文件的开头作为移动字节的参考位置。如果设为1，则使用当前的位置作为参考位置。如果它被设为2，那么该文件的末尾将作为参考位置。

fo = open("foo.txt", "a+")
print fo.tell()
fo.seek(0,0)
print fo.tell()
print fo.read(10)
print fo.tell()
fo.close()

fo = open("3.jpg", "rb+")
print fo.read(10)
fo.close()

os.remove("foo.txt")

print os.getcwd()

os.chdir("林路锋")

print os.getcwd()


os.chdir("..")

print os.getcwd()

os.rmdir("林路锋")