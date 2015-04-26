# -*- coding: utf-8 -*- 


# tuple 一旦初始化后就不可变
# tuple 中的元素类型各不相同
t = ('a', 'bbb', 3, True) # L是一个列表
print t
print len(t)

print '-------------------'

t = ()                   # empty tuple
print t
print len(t)

print '-------------------'

t1 = (1)                 # t1不是tuple，而是integer。如果要定义成tuple，则要加一个逗号，即(1,)
t2 = (1,2)
t3 = (1,)
print t1
print t2
print t3