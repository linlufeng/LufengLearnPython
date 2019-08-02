#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Python 换行

# 语句中包含 [], {} 或 () 括号就不需要使用多行连接符
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']

# 可以使用斜杠（ \）将一行的语句分为多行显示
item_one = 1
item_two = 2
item_three = 3

total = item_one + \
        item_two + \
        item_three
print total
print days