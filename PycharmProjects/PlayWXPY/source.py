#!/usr/bin/python
# -*- coding: UTF-8 -*-

from wxpy import *

bot = Bot()

my_friend = bot.friends().search('路锋', sex=MALE, city="深圳")[0]

# 微信web版不让登录没法完 over！