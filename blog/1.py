#!/bin/python


class Student(object):
    def __str__(self):
        return 'This is __str__'

    def __repr__(self):
        return 'This is __repr__'


print Student()
a = Student()
a
