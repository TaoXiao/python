# -*- encoding: utf-8 -*-
__author__ = 'tao'

from numpy import array
from numpy import tile
from numpy import random
from numpy import unique


a = array(['A', 'B', 'C'])
print "-"*10 + " a里面的数据全部是字符" +  "-"*30
print type(a)
print a
print "\n"


b = array(['A', 1, "Hello", 0.98])
print "-"*10 + " b里面的数据是不同的类型" +  "-"*30
print type(b)
print b
print "\n"


print "-"*10 + " 打印Array中的每一个元素值及其类型" +  "-"*30
for i in range(0, len(b)):
    print str(type(b[i])) + " : " + b[i]
print "\n"


# 多维数组
print "-"*10 + " 多维数组 " +  "-"*30
A = array([[1, 2, 3, 4], ['A', 'B', 'C', 'D'], ['+', '-', '*', '/']])
print A
print "\n"



# 利用tile来构造数组
print "-"*10 + " 利用tile来构造数组 " +  "-"*30
A = tile((10, 20), (4, 1))
print A   # 输出  [[10 20]
          #        [10 20]
          #        [10 20]
          #        [10 20]]

# 每个元素乘以一个数字
print A*2 # 输出 [[20 40]
          #       [20 40]
          #       [20 40]
          #       [20 40]

# 每个元素进行平方运算
print A**2  # 输出 [[100 400]
            #       [100 400]
            #       [100 400]
            #       [100 400]]

# 每个元素开方
print A**0.5
print "\n"



# 数组沿着某个轴线求和
print "-"*10 + " 数组沿着某个轴线求和 " +  "-"*30
A = array([[1,1], [2,2]])
print A
print A.sum(axis=0) # axis=0是沿着columns这一维 ，输出 [3  3]
print A.sum(axis=1) # axis=0是沿着rows这一维，输出 [2 4]
# 对于二维数组，axis只能取0或者1，对于更高维的数组，axis可以取更大的值
print "\n"


#  数组排序
print "-"*10 + " 数组排序 " +  "-"*30
A = array([10, 50, 20, 300])
print type(A)
print A
# argsort返回的是排序后的数据在原数组中的下标
idx = A.argsort()   # 输出 [0 2 1 3]
print idx

for x in idx:
    print A[x]

print "\n"

# 数组元素去重
print "-"*10 + " 数组元素去重 " +  "-"*30
A = array([1,2,1,2,1,2,1,2])
print unique(A) # 输出 [1  2]
print "\n"


# 求多维数组的最大最小值
print "-"*10 + " 求多维数组的最大最小值 " +  "-"*30
A = array([[1,3,5,7,9], [2,4,6,8,10], [-1, -3, -5, -7, -9], [-2, -4, -6, -8, -10]])
print A
print A.min(axis=0) # 纵向的最小值
print A.max(axis=0) # 纵向的最大值
print A.min(axis=1) # 横向
print A.max(axis=1)
print "\n"


# 多维数组的除法运算
# 两个数组对应元素进行相除， element-wise division
# 如果要进行矩阵除法，则要使用linalg.solve(matA, matB)
print "-"*10 + " 多维数组的除法运算 " +  "-"*30
A = array([[2,4,6,8], [20,40,60,80], [1, 3, 5, 7], [10, 30, 50, 70]])
B = array([[1,1,1,1], [2,4,6,8], [1,3,5,7,], [10, 10, 10, 10]])
print A/B






