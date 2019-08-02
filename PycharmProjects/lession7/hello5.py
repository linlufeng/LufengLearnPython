#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Python里的目录：
# 所有文件都包含在各个不同的目录下，不过Python也能轻松处理。os模块有许多方法能帮你创建，删除和更改目录。
# mkdir()方法
# 可以使用os模块的mkdir()方法在当前目录下创建新的目录们。你需要提供一个包含了要创建的目录名称的参数。
# 语法：
# os.mkdir("newdir")

import os
# mkdir()方法
# 可以使用os模块的mkdir()方法在当前目录下创建新的目录们。你需要提供一个包含了要创建的目录名称的参数。
# 语法：os.mkdir("newdir")
os.mkdir("./aaa")
# chdir()方法
# 可以用chdir()方法来改变当前的目录。chdir()方法需要的一个参数是你想设成当前目录的目录名称。
# 语法：os.chdir("newdir")
os.chdir("./aaa")
# getcwd()方法：
# getcwd()方法显示当前的工作目录。
# 语法：
# os.getcwd()
print os.getcwd()

# rmdir()方法
# rmdir()方法删除目录，目录名称以参数传递。
# 在删除这个目录之前，它的所有内容应该先被清除。
# 语法：
# os.rmdir('dirname')
os.rmdir("./aaa")

