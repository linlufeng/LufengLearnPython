
#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = 2

print isinstance(a, int)
print isinstance(a, str)
print isinstance(a, (str, int, list))
print pow(2, 3)
print pow(5, -2)
print isinstance("Hello World", basestring)
execfile("Source2.py")

class A(object):
    def aa(self):
        print "This is Class A"

class B(A):
    def bb(self):
        super(B).aa()

b = B()
b.bb()

print "B is subclass of A ? ", issubclass(B, A)
print("saas", 10.0)

