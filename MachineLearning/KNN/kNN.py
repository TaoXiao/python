# -*- encoding: utf-8 -*-
__author__ = 'tao'

##############################
##  一个简单的 K-最近邻 分类实验
##############################

from numpy import *
import operator



###############################################
# classifier
# x - 需要分类的数据，可以是多维空间中的一个点，如 (1, 3, 5, 7)
# dataSet - 训练集
# labels - 训练集对应的标签
# K - KNN 算法的参数
###############################################
def classify0(x, dataSet, labelSet, K):
    dataSetSize = dataSet.shape[0]
    # 首先计算x到训练集中每一个点的距离
    diffMat = tile(x, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat**2
    sqDist = sqDiffMat.sum(axis=1)
    dist = sqDist**0.5

    # 找出距离x最近的k个点
    sortedDistIdx = dist.argsort()

    # 开始投票
    # classCount 为 label -> vote
    classCount = {}
    for i in range(K):
        label = labelSet[sortedDistIdx[i]]
        classCount[label] = classCount.get(label, 0) + 1

    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)

    return sortedClassCount[0][0]




###############################################
# 测试产生训练数据集
###############################################
def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1], [1.1, 1.3], [1.15, 0.9]])
    labels = array(['A', 'A', 'B', 'B', 'A', 'A'])
    return group, labels

#groups, labels = createDataSet()
#print classify0(array([[0.0, 0.0]]), groups, labels, 2)
