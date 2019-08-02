#!/usr/bin/python
# -*- coding: UTF-8 -*-

class A(object):
    bar = 1

a = A()
print getattr(a, 'bar')

try:
    getattr(a, 'ss')
except:
    print "aaa"


def square(x):
    return x ** 2
print map(square, [1, 2,3])
print map(lambda x, y: x+y, range(1, 49, 2), range(2, 50, 2))

add = lambda x,y: x+y

print add(2, 3)

s = 'RUNOOB'
print repr(s)
print repr(A)


print list(xrange(0, 10, 1))

print cmp(1, 2) # -1
print cmp(1, 1) # 0
print cmp(1, 0) # 1

print max(1, 2, 5, 1009, 1000) # 1009

arr = [5, 4, 3, 2, 1]
print arr
arr.reverse()
print arr


arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
arr3 = [7, 8, 9, 10]
print zip(arr1, arr2) # [(1, 4), (2, 5), (3, 6)]
print zip(arr1, arr3) # [(1, 7), (2, 8), (3, 9)]
print zip(arr3, arr1) # [(7, 1), (8, 2), (9, 3)]
print zip(arr1, arr2, arr3) # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
