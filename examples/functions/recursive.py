# -*- coding: utf-8 -*-

print '---------- 函数递归 ----------'

def factorial(n):
	if n == 1:
		return 1
	else:
		return factorial(n-1)*n

print factorial(5)        # 返回 120	
print factorial(1000)     # RuntimeError: maximum recursion depth exceeded



