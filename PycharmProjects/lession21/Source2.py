#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import os
from requests_html import HTMLSession#必须使用session = HTMLSession()

session = HTMLSession()
os.makedirs('/Users/lufenglin/Photo/Emoji', exist_ok=True)
path = '/Users/lufenglin/Photo/Emoji/'
a = 0
fail = 0

def save(respone, name):
    with open(path+name+'.jpg','wb') as f:
        f.write(respone)

def savegif(respone, name):
    with open(path + name + '.gif', 'wb') as f:
        f.write(respone)

def src(i):
    r = session.get('https://fabiaoqing.com/biaoqing/lists/page/'+str(i)+'.html')
    for i in range(1, 46):
        div = r.html.find('#bqb > div.ui.segment.imghover > div:nth-child('+str(i)+') > a > img', first=True)
        # print(div.find('img'))#直接定位到img标签,具体分析，获取相应的数据
        try:
            print(div.attrs['data-original'])#获取到地址
            print(div.attrs['title'])#获取到title
            title = div.attrs['title']
            link = str(div.attrs['data-original'])
            print(link)
            connet = requests.get(link)
            if (link[-3:] == 'jpg'):
                save(connet.content, title)
            else:
                savegif(connet.content, title)
            # with open(path + title + '.jpg', 'wb') as f:
            #     f.write(connet.content)
        except:
            print("没有定位到超链接")
            global fail
            fail = fail + 1
        global a
        a = a + 1
        print('在下载第%d张', a)#下载了多少个
    print('失败%d张', fail)

for i in range(0,201):
    src(i)
