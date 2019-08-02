#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg


try:
    raise Networkerror("Bab hostname")
except Networkerror, e:
    print e.args