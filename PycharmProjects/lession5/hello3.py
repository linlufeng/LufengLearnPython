#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Python 字典(Dictionary)
'''
字典是另一种可变容器模型，且可存储任意类型对象。
字典的每个键值 key=>value 对用冒号 : 分割，每个键值对之间用逗号 , 分割，整个字典包括在花括号 {} 中 ,格式如下所示：
'''
dic1 = {'lin':0, 'lu':1, 'feng':2}
print dic1

# 键一般是唯一的，如果重复最后的一个键值对会替换前面的，值不需要唯一。
dic1 = {'lin':0, 'lu':1, 'feng':2, 'feng':3}
print dic1

'''
值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
一个简单的字典实例：
'''
dic2 = {'lin':0, 99:'lu', (1,2):'feng'}
print dic2
print dic2[99]
print dic2[(1,2)]

'''
访问字典里的值
把相应的键放入熟悉的方括弧，如下实例:
'''
dic3 = {'name':'linlufeng', 'age':29, 'height':163, 'weight':122}
print dic3['weight']
'''
print dic3['lin']
如果用字典里没有的键访问数据，会输出错误如下：
Traceback (most recent call last):
  File "/Users/lufenglin/PycharmProjects/lession5/hello3.py", line 26, in <module>
    print dic3['lin']
KeyError: 'lin'
'''

# 修改字典
dic3['name'] = 'wuling' # 修改
print dic3
dic3['area'] = "NanJing"# 增加
print dic3

'''
删除字典元素
能删单一的元素也能清空字典，清空只需一项操作。
显示删除一个字典用del命令，如下实例：
'''
del dic3['height'] # 删除条目 'height'
print dic3
dic3.clear()       # 清除所有条目变为 {}
print dic3
del dic3           # 删除字典

print dic2.has_key('lin')
print dic2.pop('lin')
print dic2.keys()
print dic2.values()
print dic2.items()