#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
print sys.getdefaultencoding()
reload(sys)


class A(object):
    def __init__(self):
        self.a = 1
        self.b = 2

print vars(A())