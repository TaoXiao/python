#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 在Python中，一边循环一边计算的机制，称为生成器（Generator）
# generator保存的是算法，每次调用next()，就计算出下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误
g = (x*x for x in range(10))
print g           # <generator object <genexpr> at 0x1074d3b90>
print g.next()    # 0
print g.next()    # 1
print g.next()    # 4

print '\n--- 用for来遍历generator中的内容 ---\n'

g1 = (x*x for x in range(10))
for x in g:
	print x


print '\n--- 用generator来保存fibonacci的推算规则 ---'

def fib(max):
	if max <= 0:
		yield "must larger than 0"
	n,a,b = 0,1,1
	while n < max:
		n = n+1
		if 1 == n or 2 == n:
			a = 1
			b = 1
			yield 1   # 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
		else:
			tmp = b
			b = a+b
			a = tmp
			yield b

# generator，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
for x in fib(0):
	print x


print '\n--- generator不是可重入的，是带有状态的 ---'

def odd():
	print "One"
	yield 1
	print "two"
	yield 2
	print 'three'
	yield 3

o = odd()
o.next()      # One
o.next()      # two
o.next()      # three
#o.next()      # 异常： StopIteration





