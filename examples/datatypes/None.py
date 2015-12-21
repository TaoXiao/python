#!/usr/bin/env python
# -*- encoding:utf-8 -*-

# None 有自己的数据类型: NoneType
print 'The type of None = ' + str(type(None)) # 输出 The type of None = <type 'NoneType'>

def f(x=None):
    if x == None:
        print "x is None"
    else:
        print "x is %s" % x


f("HELLO")
f(None)