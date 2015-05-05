# -*- coding:utf-8 -*-

print '-------- Basics -----------'

# 函数别名
x = abs
print x(-1)

# 数据类型转换
print int(-123)
print type(str(-123)) # <type 'str'>

#print int('123.45')   # ValueError: invalid literal for int() with base 10: '123.45'
print float('123.45') # 123.45

print bool(1) # True
print bool(2) # True
print bool(0) # False


