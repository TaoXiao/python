# -*- coding:utf-8 -*-

# for 用于 `可迭代对象`
# for 循环的形式：  
#        for x in it: 
#            doSth()


s = 'hello, world!'
for x in s:
	print x


# 迭代 dict
d = {'name':'xiaotao', 'age':30, 'Male': True}

print '--------------  迭代字典中的 key   --------------' 
for key in d:
	print key


print '--------------  迭代字典中的 value   --------------' 
for val in d.itervalues():
	print val


print '--------------  同时迭代字典中的 key 和 value   --------------' 
for k, v in d.iteritems():
	print k, v



print '--------------  怎样判断是否是 `可迭代对象`   --------------' 
from collections import Iterable
print isinstance('abc', Iterable)             # 输出  True
print isinstance(['a', 'b', 'c'], Iterable)   # 输出  True
print isinstance(d, Iterable)                 # 输出  True
print isinstance(1234, Iterable)              # 输出  False


print '--------------  在for迭代时同时输出下标   --------------' 
print '--------------  Python内置的 『enumerate』可以把 list / tuple / dict 变成 index - value pair   --------------' 
L = [100, 200, 300, 400]
for  i, v in enumerate(L):
	print i, v

T = [100, 200, 300, 400]
for  i, v in enumerate(T):
	print i, v

for  i, v in enumerate(d):
	print i, v



print '--------------  在for循环里同时引用2个变量   --------------' 
for x, y in [(1,2), (3,4), (5,6)]:
	print x, y

