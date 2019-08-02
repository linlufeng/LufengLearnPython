#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import urllib2  #将urllib2库引用进来

url="http://m.mm131.net/qingchun"
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

qqAccout = '8912462@qq.com'   #邮箱账号
qqCode = 'ujauupesnfwxcbcj'   #授权码
smtp_server = 'smtp.qq.com'
smtp_port = 465
recivers = ['849052868@qq.com', '315210770@qq.com', '8912462@qq.com']
# recivers = ['8912462@qq.com']

#配置服务器
stmp=smtplib.SMTP_SSL(smtp_server,smtp_port)
stmp.login(qqAccout,qqCode)

#组装发送内容
msgRoot = MIMEMultipart('related')
msgRoot['From'] = Header("Python邮件预警系统", 'utf-8')
msgRoot['To'] = Header("测试", 'utf-8')
subject = 'Python SMTP 邮件测试'
msgRoot['Subject'] = Header(subject, 'utf-8')
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)
mail_msg = """ <p>Python 邮件发送测试...</p> <p><a href="http://  blog.momoxiaoming.com">momoxiaoming博客</a></p> <p>图片演示：</p> <p><img  src="cid:image1"></p> """
msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8')) # 指定图片为当前目录
fp = open('girl.jpg', 'rb')   #找到程序当前目录图片
msgImage = MIMEImage(fp.read())
fp.close() # 定义图片 ID，在 HTML 文本中引用
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)


def sendText(text):
    # 组装发送内容
    message = MIMEText(text, 'plain', 'utf-8')  # 发送的内容
    message['From'] = Header("蜜汁资源在线配送", 'utf-8')  # 发件人
    message['To'] = Header("测试", 'utf-8')  # 收件人
    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')  # 邮件标题

    try:
        stmp.sendmail(qqAccout, recivers, message.as_string())
    except Exception as e:
        print '邮件发送失败--' + str(e)
    print '邮件发送成功'



sendText(conent)

'''
ujauupesnfwxcbcj pop3
yjkgluwsncrubgec CardDAV
'''