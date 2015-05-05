# -*- coding:utf-8 -*-

print '--------- 函数定义  ----------'

# 函数定义
# 如果没有return语句，则返回None
def f_abs(x):
	if (x >= 0):
		return x
	else:
		return -x

# return 与 return None 是一样的
def f_none():
	return 

print f_abs(-10)
print type(f_none) # <type 'function'>


print '--------- 空函数  ----------'

def f_nop():
	pass;

f_nop()	# 不执行任何动作
print type(f_nop()) # <type 'NoneType'>


print '--------- 函数返回类型  ----------'

# 函数签名中不含返回类型
# 一个函数可以返回不同的类型，因为python是动态类型语言
def f_ret(x):
	if x > 0 & isinstance(x, int):
		return x
	elif x == 0 :
		return 'x == 0'
	else :
		return x*1.00

print f_ret(1)   # 1
print f_ret(0)   # x == 0
print f_ret(-1)  # -1.0


print '--------- 参数类型检查  ----------'

def f_abs_check_param(x):
	# x 只能是 int类型 或者 float类型
	# not表示「非」，isinstance检查类型
	if not isinstance(x, (int, float)):
		raise TypeError('错误的数据类型')
	else:
		return f_abs(x)

#print f_abs_check_param('100')	# 	TypeError: 错误的数据类型


print '--------- 一次返回多个值  ----------'
# 语法上，返回一个tuple时可以省略括号
def f_ret_multi(x , y):
	return x, y    # 实际上是返回一个tuple

print f_ret_multi(100, 200)	 # (100, 200)
print type(f_ret_multi(1,2)) # <type 'tuple'>


