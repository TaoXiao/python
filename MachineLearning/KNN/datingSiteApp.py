# -*- encoding: utf-8 -*-
__author__ = 'tao'


from numpy import *

# 每行是一条记录
# 前3列是属性，最后1列是label，列之间用\t分隔
# 返回（matFeatures, vecLabels）
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


# 对数据进行归一化处理
# newValue = (oldValue - min)/(max-min)
# dataSet是一个多维的数组，每行是一条记录
def normalization(dataSet):
    arrMin = dataSet.min(axis=0)
    arrMax = dataSet.max(axis=0)
    arrInterval = arrMax - arrMin
    dataSetSize = dataSet.shape[0]
    normDataSet = (dataSet - tile(arrMin, (dataSetSize, 1)))/tile(arrInterval, (dataSetSize, 1))
    return normDataSet


features, labels = file2Matrix("/Users/tao/快盘/技术文档/数据挖掘与机器学习/Machine Learning in Action/datingTestSet.txt")

print normalization(features)
