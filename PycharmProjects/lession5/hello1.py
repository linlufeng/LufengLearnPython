#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Python 列表(List)
'''
序列是Python中最基本的数据结构。序列中的每个元素都分配一个数字 - 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推。
Python有6个序列的内置类型，但最常见的是列表和元组。
序列都可以进行的操作包括索引，切片，加，乘，检查成员。
此外，Python已经内置确定序列的长度以及确定最大和最小的元素的方法。
列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。
列表的数据项不需要具有相同的类型
创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。如下所示：
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]
与字符串的索引一样，列表索引从0开始。列表可以进行截取、组合等。
'''

# 访问列表中的值
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]

print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5]

# 更新列表
list = []
list.append('lin')
list.append('lu')
list.append('feng')
print list
list.pop(0)
print list
# 删除列表元素
del list[-1]
print list

'''
Python列表脚本操作符
列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表。
如下所示：

Python 表达式	                结果	                                        描述
len([1, 2, 3])	                3	                                        长度
[1, 2, 3] + [4, 5, 6]	        [1, 2, 3, 4, 5, 6]	                        组合
['Hi!'] * 4	                    ['Hi!', 'Hi!', 'Hi!', 'Hi!']	            重复
3 in [1, 2, 3]	                True	                                    元素是否存在于列表中
for x in [1, 2, 3]: print x,	1 2 3	                                    迭代
'''

list3 = ['a', 'b', 'c']
list4 = ['e', 'f', 'g']
print cmp(list3, list4)
print len(list3)
print max(list3)
print list3.count("c")
print list3.index('b')
list3.insert(1, 'p')
print list3
list3.reverse()
print list3
list3.sort()
print list3