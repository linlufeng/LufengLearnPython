#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 重命名和删除文件
# Python的os模块提供了帮你执行文件处理操作的方法，比如重命名和删除文件。
# 要使用这个模块，你必须先导入它，然后才可以调用相关的各种功能。
# rename()方法：
# rename()方法需要两个参数，当前的文件名和新文件名。
# 语法： os.rename(current_file_name, new_file_name)

import os
fo = open("test.txt", "w")
fo.close()

# 重命名
os.rename("test.txt", "lufeng.txt")

# remove()方法
# 你可以用remove()方法删除文件，需要提供要删除的文件名作为参数。
# 语法：os.remove(file_name)
# 删除
os.remove("lufeng.txt")
