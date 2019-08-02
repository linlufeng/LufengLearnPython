#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Python 循环语句 while

numbers = [1, 23, 4, 20, 19, 30]
even = []
odd = []
while len(numbers) > 0:
    number = numbers.pop()
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print "偶数有:", even
print "奇数有:", odd

count = 0
while (count < 9):
    print 'The count is:', count
    count = count + 1

print "Good bye!"

# continue 和 break 用法

i = 1
while i < 10:
    i += 1
    if i % 2 > 0:  # 非双数时跳过输出
        continue
    print i  # 输出双数2、4、6、8、10

i = 1
while 1:  # 循环条件为1必定成立
    print i  # 输出1~10
    i += 1
    if i > 10:  # 当i大于10时跳出循环
        break
'''
var = 1
while var == 1:  # 该条件永远为true，循环将无限执行下去
    num = raw_input("Enter a number  :")
    print "You entered: ", num

print "Good bye!"
'''
count = 0
while count < 5:
   print count, " is  less than 5"
   count = count + 1
else:
   print count, " is not less than 5"