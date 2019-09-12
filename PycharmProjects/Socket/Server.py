#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket                                                       # 导入 socket 模块
import sys

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()                                         # 获取本地主机名
port = 9999                                                         # 端口号
serversocket.bind((host, port))                                     # 绑定端口
serversocket.listen(5)                                              # 设置最大连接数，超过后排队

while True:
    clientsocket, addr = serversocket.accept()
    print('连接地址：%s' % str(addr))
    msg = '欢迎来到英雄联盟!' + '\r\n'
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()                                            # 关闭连接