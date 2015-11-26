# -*- encoding: utf-8 -*-
__author__ = 'tao'

from math import log


############################################################
# 计算数据集dataset的熵
# 数据集是一个二维数组，形如：
# [
#    [1, 1, 'yes'],
#    [1, 1, 'yes'],
#    [1, 0, 'no'],
#    [0, 1, 'no'],
#    [0, 1, 'no']
# ]
############################################################
def calcShannonEntropy(dataset):
    classCount = {}  # 每一种class的数量
    datasetSize = len(dataset)

    # 计算每一种class的在数据集中出现的次数
    for feature in dataset:
        classTag = feature[-1]
        if classTag not in classCount.keys():
            classCount[classTag] = 0
        classCount[classTag] += 1

    entropy = 0.0

    # 计算entropy
    for classTag in classCount.keys():
        prob = (float)(classCount[classTag])/datasetSize
        entropy -= prob*log(prob, 2)

    return entropy




############################################################
# 对数据集按照某个feature进行切分
# 其中，dataset的每个元素是一个一维数组(长度为N)，前N-1个元素每个
# 都是1个feature，最后一个元素是该数据的class tag。
# 本方法要按照第`splitIndex`个feature对数据集进行切分，
# 返回该feature的值等于`value`的所有记录
# splitIndex的范围在[0, N-1]之间：
# 返回的子集中，已经删除了splitIndex对应的feature，即返回的子集
# 中的每条记录含有N-2个feature
############################################################
def splitDataset(dataset, splitIndex, value):
    subset = []
    for t in dataset:
        if t[splitIndex] == value:
            reducedVec = t[:splitIndex]
            reducedVec.extend(t[splitIndex+1:])
            subset.append(reducedVec)
    return subset




############################################################
# 对于包含N-1个feature的数据集，从中找出信息增益最大的feature，来
# 作为该数据集的splitting criteria
############################################################
def chooseBestSplitCriteria(dataset):
    datasetSize = len(dataset)
    entropy = calcShannonEntropy(dataset)
    featNum = len(dataset[0])-1
    bestCriteria = -1
    maxInfoGain = 0.0

    for i in range(featNum): # 针对每一维的feature来计算
        featureValues = [t[0] for t in dataset]
        distinctFeatValues = set(featureValues)
        subEntropy = 0.0    # D在每一个属性处的entropy
        for v in distinctFeatValues: # 针对该feature的每一种值来计算
            subset = splitDataset(dataset, i, v)
            prob = len(subset)/float(datasetSize)
            subEntropy += prob * calcShannonEntropy(subset)
        if entropy - subEntropy > maxInfoGain: # 寻找最大的信息增益
            maxInfoGain = entropy - subEntropy
            bestCriteria = i

    return bestCriteria










dataset = [
    [1, 1, 'yes'],
    [1, 1, 'yes'],
    [1, 0, 'no'],
    [0, 1, 'no'],
    [0, 1, 'no']
]

# print(calcShannonEntropy(dataset))

print chooseBestSplitCriteria(dataset)