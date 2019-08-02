#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Python 字符串

'''
字符串是 Python 中最常用的数据类型。我们可以使用引号('或")来创建字符串。
创建字符串很简单，只要为变量分配一个值即可。例如：
'''

var1 = 'Hello World!'
var2 = "Python Runoob"

'''
Python访问字符串中的值
Python不支持单字符类型，单字符在 Python 中也是作为一个字符串使用。
Python访问子字符串，可以使用方括号来截取字符串，如下实例：
'''
print "var1[0]: ", var1[0]
print "var2[1:5]: ", var2[1:5]
print "var1[0]: ", var1[0:]

'''
Python字符串更新
你可以对已存在的字符串进行修改，并赋值给另一个变量，如下实例：
'''
print "更新字符串 :- ", var1[:6] + 'Runoob!'

'''
Python转义字符
在需要在字符中使用特殊字符时，python用反斜杠(\)转义字符。如下表：
'''

print '\\'
print '\t123'
print "\'"
print '\a123'
print '\nadc\nnike'
print '\v'


# Python字符串运算符
# 下表实例变量 a 值为字符串 "Hello"，b 变量值为 "Python"：
a = "Hello"
b = "Python"
print a+b
print a*2
print a[1]
print a[1:4]
print "H" in a
print 'e' not in a
# r/R	原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母"r"（可以大小写）以外，与普通字符串有着几乎完全相同的语法。
print r"\n"
print '\n'
print R'\n'

'''
Python 字符串格式化
Python 支持格式化字符串的输出 。尽管这样可能会用到非常复杂的表达式，但最基本的用法是将一个值插入到一个有字符串格式符 %s 的字符串中。
在 Python 中，字符串格式化使用与 C 中 sprintf 函数一样的语法。
'''
print "my name is %s, my age is %d" % ("linlufeng", 29)

print "%e" % (12100000) # 科学计数法



