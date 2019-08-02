#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Python Number(数字)

'''
Python Number 数据类型用于存储数值。
数据类型是不允许改变的,这就意味着如果改变 Number 数据类型的值，将重新分配内存空间。
以下实例在变量赋值时 Number 对象将被创建：
'''

a = 10
b = a
a = 10.0
c = a
if b is a:
    print "b is a"
else:
    print "b is not a"

'''
您可以通过使用del语句删除单个或多个对象，例如：
'''
'''
del a
print a
'''
'''
出现如下错误
Traceback (most recent call last):
  File "/Users/lufenglin/PycharmProjects/lession4/hello1.py", line 24, in <module>
    print a
NameError: name 'a' is not defined
'''


'''
整型(Int) - 通常被称为是整型或整数，是正或负整数，不带小数点。
长整型(long integers) - 无限大小的整数，整数最后是一个大写或小写的L。
浮点型(floating point real values) - 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）
复数(complex numbers) - 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。
'''
c = 2.5e2
print "c = ", c

'''
Python Number 类型转换
'''
'''
x = 3.14
print int(x)            # 将x转换为一个整数
print long(x)           # 将x转换为一个长整数
float(x)               # 将x转换到一个浮点数
# complex(real [,imag ])  # 创建一个复数
str(x)                 # 将对象 x 转换为字符串
repr(x)                # 将对象 x 转换为表达式字符串
eval(str)              # 用来计算在字符串中的有效Python表达式,并返回一个对象
tuple(s)               # 将序列 s 转换为一个元组
list(s)                # 将序列 s 转换为一个列表
chr(x)                 # 将一个整数转换为一个字符
unichr(x)              # 将一个整数转换为Unicode字符
ord(x)                 # 将一个字符转换为它的整数值
hex(x)                 # 将一个整数转换为一个十六进制字符串
oct(x)                 # 将一个整数转换为一个八进制字符串
print x
'''
