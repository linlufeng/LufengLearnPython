#!/usr/bin/python
# -*- coding: UTF-8 -*-

def aaa(str):
    "aaaaa"
    print str
    return
aaa("cccc")

# 定义函数
def printme(str):
    "打印任何传入的字符串"
    print str;
    return;


# 调用函数
printme("我要调用用户自定义函数!");
printme("再次调用同一函数");


# 可写函数说明
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4]);
    print "函数内取值: ", mylist
    return


# 调用changeme函数
mylist = [10, 20, 30];
changeme(mylist);
print "函数外取值: ", mylist


# 可写函数说明
def printinfo(name, age):
    "打印任何传入的字符串"
    print "Name: ", name
    print "Age ", age
    return;


# 调用printinfo函数
printinfo(age=50, name="miki")
printinfo("lin", 30)

def output(arg1, *vartuple):
    "biancheng"
    print "输出:"
    print arg1
    for var in vartuple:
        print var
    return

output(1, 2, 3, 4, 5)


#匿名函数
sum = lambda arg1, arg2: arg1 + arg2
print sum(1,2)

