#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Python 的字符串内建函数
'''
字符串方法是从python1.6到2.0慢慢加进来的——它们也被加到了Jython中。
这些方法实现了string模块的大部分方法，如下表所示列出了目前字符串内建支持的方法，所有的方法都包含了对Unicode的支持，有一些甚至是专门用于Unicode的。
'''

# 把字符串的第一个字符大写
print "abc".capitalize()
# 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
print "abc".center(11)

print "linlufeng".count("l", 0, 10)
print "LinLuFeng".swapcase()

'''
string.capitalize()
把字符串的第一个字符大写
string.center(width)
返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
string.count(str, beg=0, end=len(string))
返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
string.decode(encoding='UTF-8', errors='strict')
以 encoding 指定的编码格式解码 string，如果出错默认报一个 ValueError 的 异 常 ， 除非 errors 指 定 的 是 'ignore' 或 者'replace'
string.encode(encoding='UTF-8', errors='strict')
以 encoding 指定的编码格式编码 string，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
string.endswith(obj, beg=0, end=len(string))
检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
string.expandtabs(tabsize=8)
把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8。
string.find(str, beg=0, end=len(string))
检测 str 是否包含在 string 中，如果 beg 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1
string.format()
格式化字符串
string.index(str, beg=0, end=len(string))
跟find()方法一样，只不过如果str不在 string中会报一个异常.
string.isalnum()
如果 string 至少有一个字符并且所有字符都是字母或数字则返
回 True,否则返回 False
string.isalpha()
如果 string 至少有一个字符并且所有字符都是字母则返回 True,
否则返回 False
string.isdecimal()
如果 string 只包含十进制数字则返回 True 否则返回 False.
string.isdigit()
如果 string 只包含数字则返回 True 否则返回 False.
string.islower()
如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
string.isnumeric()
如果 string 中只包含数字字符，则返回 True，否则返回 False
string.isspace()
如果 string 中只包含空格，则返回 True，否则返回 False.
string.istitle()
如果 string 是标题化的(见 title())则返回 True，否则返回 False
string.isupper()
如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
string.join(seq)
以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
string.ljust(width)
返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
string.lower()
转换 string 中所有大写字符为小写.
string.lstrip()
截掉 string 左边的空格
string.maketrans(intab, outtab])
maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
max(str)
返回字符串 str 中最大的字母。
min(str)
返回字符串 str 中最小的字母。
string.partition(str)
有点像 find()和 split()的结合体,从 str 出现的第一个位置起,把 字 符 串 string 分 成 一 个 3 元 素 的 元 组 (string_pre_str,str,string_post_str),如果 string 中不包含str 则 string_pre_str == string.
string.replace(str1, str2,  num=string.count(str1))
把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次.
string.rfind(str, beg=0,end=len(string) )
类似于 find()函数，不过是从右边开始查找.
string.rindex( str, beg=0,end=len(string))
类似于 index()，不过是从右边开始.
string.rjust(width)
返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
string.rpartition(str)
类似于 partition()函数,不过是从右边开始查找
string.rstrip()
删除 string 字符串末尾的空格.
string.split(str="", num=string.count(str))
以 str 为分隔符切片 string，如果 num有指定值，则仅分隔 num 个子字符串
string.splitlines([keepends])
按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
string.startswith(obj, beg=0,end=len(string))
检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查.
string.strip([obj])
在 string 上执行 lstrip()和 rstrip()
string.swapcase()
翻转 string 中的大小写
string.title()
返回"标题化"的 string,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
string.translate(str, del="")
根据 str 给出的表(包含 256 个字符)转换 string 的字符,
要过滤掉的字符放到 del 参数中
string.upper()
转换 string 中的小写字母为大写
string.zfill(width)
返回长度为 width 的字符串，原字符串 string 右对齐，前面填充0
'''