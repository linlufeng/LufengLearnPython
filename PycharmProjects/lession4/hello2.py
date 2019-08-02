#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Python 数学函数
import math
# 返回数字的绝对值，如abs(-10) 返回 10
print abs(-10)

# ceil(x)	返回数字的上入整数，如math.ceil(4.1) 返回 5
print math.ceil(4.1)

# 如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1
x = 1
y = 2
print cmp(x, y)
a = 1
b = 1
print cmp(a, b)
c = 3
d = 2
print cmp(c, d)

# 返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
print math.exp(1)

# 返回数字的绝对值，如math.fabs(-10) 返回10.0
print math.fabs(-3.14)

# 返回数字的下舍整数，如math.floor(4.9)返回 4
print math.floor(4.9)

# 如math.log(math.e)返回1.0,math.log(100,10)返回2.0
print math.log(100, 10)

# 返回以10为基数的x的对数，如math.log10(100)返回 2.0
print math.log10(100)

# 返回给定参数的最大值，参数可以为序列。
print max(1, 3, 5, 100, 9, 8)

# 返回给定参数的最小值，参数可以为序列。
print min(10, 9, 8, 7, 6)

# modf(x) 返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。

# pow(x, y)	x**y 运算后的值。
print pow(2, 3)

# round(x [,n])	返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
print round(3.1415926, 3)

# sqrt(x)	返回数字x的平方根
print math.sqrt(2)