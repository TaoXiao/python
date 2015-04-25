#!/usr/bin/env python
# -*- encoding:utf-8 -*-

age = raw_input()  # 即使输入10，输出仍然是 age > 18
if age > 18:
	print 'age > 18'
elif age == 18:
	print 'age == 18'
else:
	print 'age < 18';


age = input()	# 现在输入的字符串可以被转换为int，可以输出正确的比较结果
if age > 18:
	print 'age > 18'
elif age == 18:
	print 'age == 18'
else:
	print 'age < 18';