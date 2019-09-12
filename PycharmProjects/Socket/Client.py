#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket
import sys

s = socket.socket()             # 创建 socket
host = socket.gethostname()
port = 9999

s.connect((host, port))
s.send('ssss'.encode('utf-8'))
msg = s.recv(1024)
s.close()
print(msg.decode('utf-8'))

