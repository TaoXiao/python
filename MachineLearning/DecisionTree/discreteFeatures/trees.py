# -*- encoding: utf-8 -*-
__author__ = 'tao'

from math import log
import operator
import json


############################################################
## 本例中的代码只能计算nominal类型的数据
## 如果是连续性数据，则还要加以转换
############################################################



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
    for t in dataset:
        classTag = t[-1]
        if classTag not in classCount.keys():
            classCount[classTag] = 0
        classCount[classTag] += 1

    # 计算entropy
    entropy = 0.0
    for classTag in classCount.keys():
        prob = classCount[classTag]/float(datasetSize)
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
    baseEntropy = calcShannonEntropy(dataset) # 数据集D的熵
    featNum = len(dataset[0])-1 # feature的数量（维度）
    bestCriteria = -1 # 最佳split属性的index
    maxInfoGain = 0.0

    for i in range(featNum): # 针对每一维的feature来计算
        featureValues = [t[i] for t in dataset]
        distinctFeatValues = set(featureValues)
        subEntropy = 0.0    # D在每一个属性处的entropy
        for v in distinctFeatValues: # 针对该feature的每一种值来计算
            subset = splitDataset(dataset, i, v)
            prob = len(subset)/float(datasetSize)
            subEntropy += prob * calcShannonEntropy(subset)
            # 调试用：
            # print "attribute index -> ", i, "\t subEntropy -> ", subEntropy,
            # "\t info gain -> ", baseEntropy - subEntropy
        if baseEntropy - subEntropy > maxInfoGain: # 寻找最大的信息增益
            maxInfoGain = baseEntropy - subEntropy
            bestCriteria = i

    return bestCriteria





############################################################
# 找出最主流的class(按照频率计算)
############################################################
def majorClass(classList):
    classCountMap = {}
    for clz in classList:
        if clz not in classCountMap.keys():
            classCountMap[clz] = 1
        else:
            classCountMap[clz] += 1
    # 按照value进行排序，并返回频次最高的class的tag
    return sorted(classCountMap.iteritems(), key=operator.itemgetter(1), reverse=True)[0][0]




############################################################
# 为一个数据集(nominal类型)构建一颗decision tree
# attrLabels是所有attribues label的列表，其中的label的顺序
# 与dataeset中每个tuple中的attribute value的顺序必须是一致的
############################################################
def createDecisionTree(dataset, featLabels):
    classValueList = [t[-1] for t in dataset]  # 取出全部的class values

    # 如果dataset中全部的数据都属于同一个class，则返回该class
    if classValueList.count(classValueList[0]) == len(classValueList):
        return classValueList[0]

    # 如果dataset中已经没有attribute了，则返回所有class中的majority
    if (len(dataset[0]) == 1):
        return majorClass(classValueList)

    # 找出目前dataset中最重要的feature的index
    bestFeatIdx = chooseBestSplitCriteria(dataset)
    bestFeatLabel = featLabels[bestFeatIdx]
    subFeatLabels = featLabels[:]
    tree = {bestFeatLabel:{}} # 构造根节点

    # 下面处理根节点的每一个branch
    del(subFeatLabels[bestFeatIdx])  # 去掉这个feature label
    featValueSet = set([x[bestFeatIdx] for x in dataset])
    for featValue in featValueSet:
        tree[bestFeatLabel][featValue] = createDecisionTree(
            splitDataset(dataset, bestFeatIdx, featValue),
            subFeatLabels)

    return tree




############################################
# 下面用数据来测试
############################################
def createDataset():
    dataset = [
        [1, 1, 'yes'],
        [1, 1, 'yes'],
        [1, 0, 'no'],
        [0, 1, 'no'],
        [0, 1, 'no']
    ]
    labels = ["Survive", "Fish"]
    return dataset, labels


def test1():
    dataset, labels = createDataset()
    print json.dumps(createDecisionTree(dataset, labels), indent=4)


############################################################
# 再用一组新数据来测试
# 数据来源：《Data Mining: Concepts and Techniques》
############################################################
def generateDataSet():
    dataset = [
        ['youth',       'high',     'no',   'fair',         'no'],
        ['youth',       'high',     'no',   'excellent',    'no'],
        ['middle_aged', 'high',     'no',   'fair',         'yes'],
        ['senior',      'medium',   'no',   'fair',         'yes'],
        ['senior',      'low',      'yes',  'fair',         'yes'],
        ['senior',      'low',      'yes',  'excellent',    'no'],
        ['middle_aged', 'low',      'yes',  'excellent',    'yes'],
        ['youth',       'medium',   'no',   'fair',         'no'],
        ['youth',       'low',      'yes',  'fair',         'yes'],
        ['senior',      'medium',   'yes',  'fair',         'yes'],
        ['youth',       'medium',   'yes',  'excellent',    'yes'],
        ['middle_aged', 'medium',   'no',   'excellent',    'yes'],
        ['middle_aged', 'high',     'yes',  'fair',         'yes'],
        ['senior',      'medium',   'no',   'excellent',    'no']
    ]
    labels = ['age', 'income', 'student', 'credit_rating', 'buys_computer']
    return dataset, labels


def test2():
    dataset, labels = generateDataSet()
    print json.dumps(createDecisionTree(dataset, labels), indent=4)



############################################################
# 用MLLib中的数据进行训练
# 数据是一个CSV文件，来源于
############################################################
def readCSVDataSet(path):
    import csv
    dataset = []
    with open(path, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            for field in row:
                print field, type(field)
            return


readCSVDataSet("/Users/tao/Downloads/sample_tree_data.csv")