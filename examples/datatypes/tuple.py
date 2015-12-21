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
print t2[0], t2[1]      # 取出一个tuple中的某个元素，按照位置取


print '-------------------'

def test():
    x = (1,2,3)
    (a,b,c) = x
    return a, b, c

(z1, z2, z3) = test()
print z1
print z2
print z3
