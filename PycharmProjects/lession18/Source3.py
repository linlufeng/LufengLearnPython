#!/usr/bin/python
# -*- coding: UTF-8 -*-
# super 实例

class FooParent(object):
    def __init__(self):
        self.parent = "I\'m the parent."
        print ('Parent')

    def bar(self, message):
        print ("%s from Parent" % message)


class FooChild(FooParent):
    def __init__(self):
        super(FooChild.self).__init__()
        print ('Child')

    def bar(self, message):
        super(FooChild, self).bar(message)
        print ('Child bar fuction')
        print (self.parent)


if __name__ == '__main__':
    fooChild = FooChild()
    fooChild.bar('HelloWorld')
