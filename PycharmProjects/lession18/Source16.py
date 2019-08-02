#!/usr/bin/python
# -*- coding: UTF-8 -*-

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

myslice = slice(5)
hisslice = slice(0, 10, 2)
print arr[myslice] # [1, 2, 3, 4, 5]
print arr[hisslice] # [1, 3, 5, 7, 9]
print id(myslice)


print oct(66)

a = [5, 7, 6, 3, 4, 1, 2]
b = sorted(a)
print b # [1, 2, 3, 4, 5, 6, 7]

print sorted(a, cmp=lambda x, y: cmp(x,y))

L = [('b', 2), ('a', 1), ('c', 3), ('d', 4)]
print sorted(L, cmp=lambda x,y:cmp(x[1],y[1])) # [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
print sorted(L, key=lambda x:x[1]) # [('a', 1), ('b', 2), ('c', 3), ('d', 4)]


exec("for i in range(5): print i")