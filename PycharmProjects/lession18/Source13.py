#!/usr/bin/python
# -*- coding: UTF-8 -*-

str = "for i in range(0, 10, 1): print(i)"
code = compile(str, '', 'exec')
exec(code)
