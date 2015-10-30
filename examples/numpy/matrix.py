# -*- encoding: utf-8 -*-
__author__ = 'tao'

from numpy import *

# Random Array
randArr = random.rand(4, 4)
print "-"*10 + " `randArr` " +  "-"*30
print type(randArr)
print randArr
print "\n"


# Matrix （Array => Matrix）
randMat = mat(randArr)
print "-"*10 + " `randMat` " +  "-"*30
print type(randMat)
print randMat
print "\n"


# Inverse matrix (逆矩阵)
invRandMat = randMat.I
print "-"*10 + " `invRandMat` " +  "-"*30
print type(invRandMat)
print invRandMat
print "\n"


# 矩阵相乘
print "-"*10 + " 矩阵 * 逆矩阵 = 单位矩阵 " +  "-"*30
print randMat*invRandMat
print "\n"


# 用eye(n)方法构造单位矩阵，indentity matrix
print "-"*10 + " 构造 单位矩阵 " +  "-"*30
print eye(4)
print "\n"


# 查看一个矩阵的维度
print  "-"*10 + " 矩阵的维度 " +  "-"*30
A = mat(random.rand(2, 4))
print type(A)     # 输出 <class 'numpy.matrixlib.defmatrix.matrix'>
print A
print A.shape
print A.shape[0]
print A.shape[1]
print "\n"


# 用 tile 对已有数据进行重复，来创建一个Array
# 注意： Array不是Matrix ！！！
print  "-"*10 + " 用 tile 对已有数据进行重复，来创建一个Array " +  "-"*30
A = array([10,20,30])
print type(A)           # 输出 <type 'numpy.ndarray'>
print tile(A, 3)        # 输出 [10 20 30 10 20 30 10 20 30]
print tile(A, (2,4))    # 输出 [[10 20 30 10 20 30 10 20 30 10 20 30]
                        #       [10 20 30 10 20 30 10 20 30 10 20 30]]

print tile(9, (2, 4))   # 输出 [[9 9 9 9]
                        #       [9 9 9 9]]

print tile(('x', 'y'), (3, 4))   # 输出 [['x' 'y' 'x' 'y' 'x' 'y' 'x' 'y']
                                 #       ['x' 'y' 'x' 'y' 'x' 'y' 'x' 'y']
                                 #       ['x' 'y' 'x' 'y' 'x' 'y' 'x' 'y']]

print "\n"

# 矩阵运算

# 相同维度的矩阵的相减运算
# 不同维度的矩阵不能进行加减法运算
# 注意： tile 构造出的不是matrix，而是array

# 矩阵的乘法
print  "-"*10 + " 矩阵与一个数字相乘 " +  "-"*30
A = mat(array([[1,2,3], [4,5,6], [100, 200, 300]]))
print A

print  "-"*10 + " 矩阵与一个数字相乘 " +  "-"*30
print A*2

print  "-"*10 + " 矩阵自乘N次" +  "-"*30
print A**2



print  "-"*10 + " 矩阵与一个数字相乘 " +  "-"*30
A = mat(random.rand(4,2))
print A
#print A**2



