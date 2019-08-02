#!/usr/bin/python
# -*- coding: UTF-8 -*-

print bytearray('sdsa23', 'utf-8')

print float(1)

print unichr(97)
print unichr(66)

print "{} {}".format("hello", "world")
print "{0} {1}".format("hello", "world")
print "{1} {0} {1}".format("hello", "world")

print "网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com")

site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))

# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的


class AssignValue(object):
    def __init__(self, value):
        self.value = value
myValue = AssignValue(6)
print('value 为: {0.value}'.format(myValue))

# locals() 函数会以字典类型返回当前位置的全部局部变量。
def runoob(arg):
    z = 1
    print locals()

runoob(5)


def add(x, y):
    return x+y

print reduce(add, [1, 2, 3, 4, 5])
print reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])

print chr(97)

a = frozenset(range(10))

print long(1)
print long('1234')