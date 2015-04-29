# -*- coding:utf-8 -*-

a = set([1,2,3]) # 不能写成a = set(1,2,3)
print a    # set([1, 2, 3]), a中的元素并不是一个list
print len(a) # 3

for x in a :
	print x

print '-----------------'

# 添加10
a.add(10)
print a

# 删除10
a.remove(10)
print a

print '-----------------'

a1 = set([1,2,3,4])
a2 = set([2,4,6])
print a1 & a2  # intersection
print a1 | a2  # union

print '-----------------'

# set允许不同类型的数据
x = set(['A', 'B', 'C', 100, 200, 300])
print x