#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib2  #将urllib2库引用进来

url="https://n.cbg.163.com/cbg/query.py?serverid=7&act=search_role"
#要伪装的浏览器user_agent头
user_agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36;"
#创建字典，使请求的headers中的’User-Agent‘：对应user_agent字符串
headers={'User-Agent':user_agent}
#新建一个请求，将请求中的headers变换成自己定义的
req =urllib2.Request(url,headers=headers)
#请求服务器，得到回应
response=urllib2.urlopen(req)
#得到回应内容
conent=response.read()
#打印结果
print conent


