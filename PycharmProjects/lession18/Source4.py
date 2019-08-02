#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Human(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def infomation(self):
        print "name is ", self.name
        print "age is ", self.age
        print "sex is ", self.sex

man = Human("lufeng", 30, 1)
man.infomation()


class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print "Ahahaha"
        else:
            print "No Thanks!"

class SongBird(Bird):
    def __init__(self):
        Bird.__init__(self)
        self.sound = "SJKSJSK"
    def sing(self):
        print self.sound

sb = SongBird()
sb.sing()
sb.eat()

print bin(5)


fo = file("1.txt", "a+")
fo.write("aaa")
fo.close()


array = [1, 2, 3, 4]
it = iter(array)
print array.pop()
print array
array.append(5)
print array
print it.next()
for i in it:
    print i