#!/usr/bin/env python
# encoding=utf-8

def calculate(first, second):
    return u"%(first)s -> %(second)s" % {'first': first, 'second': second}

print "calculate(5, 3): %s" % calculate(5, 3)

print "calculate(second=3, first=5): %s" % calculate(second=3, first=5)

def calculate2(**variables):
    return u"%(first)s -> %(second)s" % {'first': variables['first'], 'second': variables['second']}

print "calculate2(second=3, first=5): %s" % calculate2(second=3, first=5)
