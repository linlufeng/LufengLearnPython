#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
检索和替换
Python 的 re 模块提供了re.sub用于替换字符串中的匹配项。
语法：
re.sub(pattern, repl, string, count=0, flags=0)
参数：
pattern : 正则中的模式字符串。
repl : 替换的字符串，也可为一个函数。
string : 要被查找替换的原始字符串。
count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
'''

import re

phone = "2004-959-559 # 这是一个国外电话号码"

# 删除字符串中的 Python注释
num = re.sub(r'#.*$', "", phone)
print "电话号码是: ", num

# 删除非数字(-)的字符串
num = re.sub(r'\D', "", phone)
print "电话号码是 : ", num

'''
repl 参数是一个函数
以下实例中将字符串中的匹配的数字乘以 2：
'''


# 将匹配的数字乘以 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)


s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))

'''
re.compile 函数
compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
语法格式为：
re.compile(pattern[, flags])
'''

'''
lufeng:~ lufenglin$ python
Python 2.7.10 (default, Oct  6 2017, 22:29:07) 
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.31)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import re
>>> pattern = re.compile(r'\d+')
>>> m = pattern.match('one12twothree34four')
>>> print m
None
>>> m = pattern.match('one12twothree34four',2,10)
>>> print m
None
>>> m = pattern.match('one12twothree34four',3,10)
>>> print m
<_sre.SRE_Match object at 0x10b5adb28>
>>> m.group(0)
'12'
>>> m.start(0)
3
>>> m.end(0)
5
>>> m.span(0)
(3, 5)
>>> 
'''

'''
在上面，当匹配成功时返回一个 Match 对象，其中：
group([group1, …]) 方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用 group() 或 group(0)；
start([group]) 方法用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），参数默认值为 0；
end([group]) 方法用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为 0；
span([group]) 方法返回 (start(group), end(group))。
'''


'''
lufeng:~ lufenglin$ python
Python 2.7.10 (default, Oct  6 2017, 22:29:07) 
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.31)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import re
>>> pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)
>>> m = pattern.match('Hello World Wide Web')
>>> print m
<_sre.SRE_Match object at 0x102eb78b0>
>>> m.group(0)
'Hello World'
>>> m.span(0)
(0, 11)
>>> m.group(1)
'Hello'
>>> m.group(2)
'World'
>>> m.span(2)
(6, 11)
>>> m.span(1)
(0, 5)
>>> m.groups()
('Hello', 'World')
>>> m.group(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: no such group
>>> 
'''
'''
findall
在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
注意： match 和 search 是匹配一次 findall 匹配所有。
语法格式为：
findall(string[, pos[, endpos]])
参数：
string : 待匹配的字符串。
pos : 可选参数，指定字符串的起始位置，默认为 0。
endpos : 可选参数，指定字符串的结束位置，默认为字符串的长度。
查找字符串中的所有数字：
'''
# 实例
'''
lufeng:~ lufenglin$ python
Python 2.7.10 (default, Oct  6 2017, 22:29:07) 
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.31)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import re
>>> pattern = re.compile(r'\d+')
>>> result1 = pattern.findall('runoob 123 google 456')
>>> result2 = pattern.findall('run99oob123google456',0,10)
>>> print(result1)
['123', '456']
>>> print(result2)
['99', '12']
>>> 
'''

'''
re.finditer
和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
re.finditer(pattern, string, flags=0)
参数：
参数	描述
pattern	匹配的正则表达式
string	要匹配的字符串。
flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。参见：正则表达式修饰符 - 可选标志
'''
it = re.finditer(r"\d+","12a32bc43jf3")
for match in it:
    print (match.group())