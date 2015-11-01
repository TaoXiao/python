# -*- encoding: utf-8 -*-
__author__ = 'tao'


from numpy import *
import kNN

#######################################
# 读取文件里的训练集，并提取出其中的features与labels
# 每行是一条记录，形如：
#   40920   8.326976    0.953952	largeDoses

# 前3列是属性，最后1列是label，列之间用\t分隔
# 返回（matFeatures, vecLabels）
#######################################
def file2Matrix(path):
    f = open(path)
    lines = f.readlines()
    numLines = len(lines) # 返回文件的行数
    matFeatures = zeros((numLines, 3))  # 创建一个指定shape和type的array，用0初始化
    vecLabels = []   # vecLabels是一个List

    i = 0
    for line in lines:
        tokens = line.strip().split("\t")
        matFeatures[i, :] = tokens[0:3]
        vecLabels.append(tokens[-1])
        i += 1

    return matFeatures, vecLabels


#######################################
# 归一化处理
# newValue = (oldValue - min)/(max-min)
# dataSet是一个多维的数组，每行是一条记录
#######################################
def normalization(dataSet):
    arrMin = dataSet.min(axis=0)
    arrMax = dataSet.max(axis=0)
    arrRange = arrMax - arrMin
    dataSetSize = dataSet.shape[0]
    normDataSet = (dataSet - tile(arrMin, (dataSetSize, 1)))/tile(arrRange, (dataSetSize, 1))
    return normDataSet, arrMin, arrRange



#######################################
# calcErrorRate
# 计算kNN预测算法应用于dating site数据时的错误率
# 将数据集中的的部分数据作为训练数据，其余作为测试数据
# holdOutRatio  : 选取前N条记录来测试预测错误率
#######################################
def calcErrorRate(features, lables, holdOutRatio):
    testCount = int(features.shape[0]*holdOutRatio)
    errorCount = 0.0
    for i in range(testCount):
        predictedLabel = kNN.classify0(features[i, :], features, labels, 3)
        realLabel = labels[i]
        print "predicted : " + predictedLabel + "\t\treal : " + realLabel
        if predictedLabel != realLabel :
            errorCount += 1.0
    return errorCount/testCount



features, labels = file2Matrix("/Users/tao/快盘/技术文档/数据挖掘与机器学习/Machine Learning in Action/datingTestSet.txt")


x = [4.09200000e+04,   8.32697600e+00,   9.53952000e-01]
normFeatures, arrMin, arrRange = normalization(features)
