#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件定位
# tell()方法告诉你文件内的当前位置, 换句话说，下一次的读写会发生在文件开头这么多字节之后。
# seek（offset [,from]）方法改变当前文件的位置。Offset变量表示要移动的字节数。From变量指定开始移动字节的参考位置。
# 如果from被设为0，这意味着将文件的开头作为移动字节的参考位置。如果设为1，则使用当前的位置作为参考位置。如果它被设为2，那么该文件的末尾将作为参考位置。
# 例子：
# 就用我们上面创建的文件foo.txt。

# 打开文件
fo = open("foo.txt")
str = fo.read(10)
print "read content is ", str

# 查找当前位置
position = fo.tell()
print "file current position is ", position


# 把指针再次重新定位到文件开头
position = fo.seek(0, 0)
str = fo.read(10)
print "reread file content is : ", str
# 关闭打开的文件
fo.close()