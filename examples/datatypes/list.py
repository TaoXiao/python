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


print '-------------------'

L.append('hello')        # List是可变的
print L[-1]
L.insert(1, 'x')         # 指定在为止1上插入新元素，其余元素后移一位
print L

print '-------------------'

x = L.pop()              # pop 弹出并删除最后一个元素
print 'x = %s, L = %s' % (x, L)
y = L.pop(1)             # pop(i) 弹出并删除第i个元素
print 'y = %s, L = %s' % (y, L)


print '-------------------'

L = []                   #  L是空数组，长度为0
print len(L)





