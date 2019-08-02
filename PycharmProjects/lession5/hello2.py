#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Python 元组

'''
Python的元组与列表类似，不同之处在于元组的元素不能修改。
元组使用小括号，列表使用方括号。
元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
'''
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"

print list(tup1)
# 创建空元组
tup4 = ()
# 元组中只包含一个元素时，需要在元素后面添加逗号
tup5 = (51,)

# 访问元组
print "tup1[0]: ", tup1[0]
print "tup2[1:5]: ", tup2[1:5]

# 修改元组
'''
元组中的元素值是不允许修改的，但我们可以对元组进行连接组合，如下实例:
'''
# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 创建一个新的元组
tup6 = tup1 + tup2
print tup6

# 删除元组
# 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组，如下实例:
tup = ('physics', 'chemistry', 1997, 2000)

print tup
del tup
print "After deleting tup : "
print tup