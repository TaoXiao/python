#!/usr/bin/env python
# -*- coding:utf-8 -*-

s1 = 'I\'m Xiao Tao'
s2 = "I'm also Xiao Tao"

print s1
print s2

print '--------------'

s3 = r'这里的\不转义'
print s3

print '--------------'

# 替换字符
# 字符串本身是immutable
x = "ABCABC"
y = x.replace('A', 'a')
print x # 输出  ABCABC
print y # 输出  aBCaBC 



