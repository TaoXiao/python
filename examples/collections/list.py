# -*- coding:utf-8 -*-


# List是可变的（tuple是不可变的），其中的各元素可以不同类型
L = ['a', 'bbb', 3, True] # L是一个列表
print L
print len(L)             # len(L)可以求出列表的长度

print '-------------------'
	
# 索引下标用方括号表示	
print L[0]               
print L[len(L)-1]

print '-------------------'
print L[-1]              # -1表示倒数第一个位置
print L[-len(L)]


print '\n--------追加/插入元素-----------'

L.append('hello')        # List是可变的
print L[-1]
L.insert(1, 'x')         # 指定在位置1上插入新元素，其余元素后移一位
print L

print '\n-------弹出/删除元素------------'
print 'L = %s' % L
x = L.pop()              # pop 弹出并删除最后一个元素
print 'x = %s, L = %s' % (x, L)
y = L.pop(1)             # pop(i) 弹出并删除第i个元素
print 'y = %s, L = %s' % (y, L)
del(L[0])                # del(L[i]) 直接删除L中的第i个元素
print L


print '\n--------空列表-----------'
L = []                   #  L是空数组，长度为0
print len(L)



print '\n--------找出某个值出现的次数-----------'
L = [1,2,3,3,4,5,6,7,7,7,8]
print L.count(7)


print '\n--------克隆一个List-----------'
A = [1,2,3,4]
B = A[:]# 或者B = [x for x in A]
A[0] = 100 # A 和 B 是两个独立的List
print A
print B




