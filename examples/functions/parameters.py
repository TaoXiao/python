# -*- coding:utf-8 -*-

print '------- 默认参数 ---------'

# 计算x的n次方
# 这里参数n的默认值为2
def power(x, n=2): 
	sum = 1
	if 0 == n:
		return 1
	else:
		while n > 0:
			sum = sum * x
			n = n - 1
	return sum

print power(3)
print power(3,3)

# 『默认参数』必须在『必选参数』的后面
def f_default_param(name, gender='Male', city='NJ'):
	print (name, gender, city)

f_default_param('Tom')             # 输出 ('Tom', 'Male', 'NJ')

# 调用时可以打乱传入参数的顺序，但是必须指定参数名
f_default_param('Jim', city='SH')  # 输出 ('Jim', 'Male', 'SH')



print '------- a pit fall ---------'



# 定义默认参数要牢记一点：默认参数必须指向immutable对象！
def f_add_end(L = []):
	L.append('end')
	return L

print f_add_end()  # 输出 ['end']
print f_add_end()  # 输出 ['end', 'end'] 
print f_add_end()  # 输出 ['end', 'end', 'end']
# 原因解释如下：
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]。
# 因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。

# 修改如下：用None这个 immutable object 来实现 ！

def f_add_end(L = None):
	if L is None:
		print 'L is None; '
		L = []
	L.append('end')
	return L

print f_add_end()  # 输出  L is None; ['end']
print f_add_end()  # 输出  L is None; ['end'] 
print f_add_end()  # 输出  L is None; ['end']	



print '------- 可变参数 ---------'


# 形参前面加上*号，就成为了可变形参
# 传入的可变参数才调用时被自动组装成了一个tuple
def f_variable_param(*numbers):
	sum = 0 
	for x in numbers:
		sum = sum + x*x
	return sum

print f_variable_param(1,2,3)	# 输出 14

# 可以传入0个实参
print f_variable_param()        # 输出 0

# 实参（list或者tuple）前面加上*号，就成为了可变实参
t = (1 ,2, 3)
print f_variable_param(*t)      # 输出 14
l = [1, 2, 3]	
print f_variable_param(*l)      # 输出 14



print '------- 关键字参数 ---------'



# 关键字参数允许你传入0个或任意个含参数名的参数，
# 这些关键字参数在函数内部自动组装为一个dict

def f_kw_param(name, age, **kw):
	print 'name = ', name,  ', age = ', age, ', kw = ' , kw

# 输出  	name =  xt , age =  30, kw =  {}
f_kw_param('xt', 30)    

# 输出  name =  xt , age =  30, kw  =  {'city': 'Nanjing'}
f_kw_param('xt', 30, city='Nanjing')

# 输出  name =  xt , age =  30, kw =  {'province': 'Jiangsu', 'city': 'Nanjing'}
f_kw_param('xt', 30, city='Nanjing', province='Jiangsu')

# 调用错误： TypeError: f_kw_param() takes exactly 2 arguments (3 given)
#f_kw_param('xt', 30, 'Nanjing')  



print '------- 将dict作为关键字参数传递 ---------'



d = { 'province': 'Jiangsu', 'city': 'Nanjing' }

# 输出 name =  xt , age =  30 , kw =  {'keyword': {'province': 'Jiangsu', 'city': 'Nanjing'}}
f_kw_param('xt', 30, keyword = d)

# 输出 name =  xt , age =  30 , kw =  {'province': 'Jiangsu', 'city': 'Nanjing'}
f_kw_param('xt', 30, **d)




print '------- 参数组合  ---------'


#  组合参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。

def f_comb_param(a, b, c = 888, *d, **e):
	print 'a=', a, " | b=", b, " | c=", c, " | d=", d, " | e=", e

# a= 100  | b= 200  | c= 888  | d= ()  | e= {}
f_comb_param(100, 200)

# a= 100  | b= 200  | c= 300  | d= ()  | e= {}
f_comb_param(100, 200, 300)

# a= 100  | b= 200  | c= 300  | d= (400,)  | e= {}
f_comb_param(100, 200, 300, 400)

# a= 100  | b= 200  | c= 300  | d= (400,)  | e= {}
f_comb_param(100, 200, 300, 400)

# a= 100  | b= 200  | c= 300  | d= (400, 500)  | e= {}
f_comb_param(100, 200, 300, 400, 500)

# a= 100  | b= 200  | c= 300  | d= (400,)  | e= {'d': 500}
f_comb_param(100, 200, 300, 400, d = 500)

# a= 100  | b= 200  | c= 300  | d= (400,)  | e= {'d': (1, 2, 3)}
f_comb_param(100, 200, 300, 400, d = (1,2,3))

# a= 100  | b= 200  | c= 300  | d= ((400, 500),)  | e= {'d': (1, 2, 3)}
f_comb_param(100, 200, 300, (400, 500), d = (1,2,3))

# a= 100  | b= 200  | c= 300  | d= (400, 500)  | e= {'d': (1, 2, 3)}
f_comb_param(100, 200, 300, *(400, 500), d = (1,2,3))




