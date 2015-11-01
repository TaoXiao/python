# -*- encoding: utf-8 -*-
__author__ = 'tao'

from numpy import zeros
import os
import kNN

KNN_K = 3

###################################
# 利用KNN算法来预测手写数字的真实值
# 这个算法相当耗时（计算距离的次数很多）
# 改进：使用 kD-trees
###################################



############################################
# 将文件中的图像数据转换成一个 1x1024 的一维数组
# 文件共有32行，每行有32个数字
############################################
def img2vector(filePath):
    vec = zeros(1024)
    f = open(filePath)
    lines = f.readlines()

    for lineNum in range(32):   # 文件有32行
        for i in range(32):   # 每行有32个字符
            vec[i + lineNum*32] = lines[lineNum][i]
    return vec




############################################
# 解析一个目录下的文件，每个文件是一条训练数据
# 文件名的第一个字符代表该条训练数据的真实class（0 ~ 9）
############################################
def parseImgsDir(dirPath):
    files = os.listdir(dirPath)
    dataSetSize = len(files)
    labelSet = []
    dataSet = zeros((dataSetSize, 1024))

    i = 0
    for file in files:
        filePath = os.path.join(dirPath, file)
        dataSet[i] = img2vector(filePath) # 一条训练数据
        labelSet.append(file[0]) # 文件名的第一个字符为label
        i+=1

    return dataSet, labelSet





############################################
# 测试误差率
############################################
def calcErrorRate(trainingFeatureSet, trainingLabelSet, testDataDir):
    testFiles = os.listdir(testDataDir)
    testDataSetSize = len(testFiles)

    errorCount = 0.0

    for file in testFiles:
        filePath = os.path.join(testDataDir, file)
        testData = img2vector(filePath)
        trueLabel = file[0] # 测试数据的真实label
        predictedLabel = kNN.classify0(testData, trainingFeatureSet, trainingLabelSet, KNN_K)
        if predictedLabel != trueLabel:
            errorCount += 1
            print "Predicted : ", predictedLabel, "    True : " , trueLabel, "   File : ",  file

    return errorCount/testDataSetSize




# 测试
trainingFeatureSet, trainingLabelSet = parseImgsDir("/Users/tao/快盘/技术文档/数据挖掘与机器学习/Machine Learning in Action/ch02/digits/trainingDigits")
testDataFeature = img2vector("/Users/tao/快盘/技术文档/数据挖掘与机器学习/Machine Learning in Action/ch02/digits/testDigits/9_60.txt")
print calcErrorRate(trainingFeatureSet, trainingLabelSet, "/Users/tao/快盘/技术文档/数据挖掘与机器学习/Machine Learning in Action/ch02/digits/testDigits")
print kNN.classify0(testDataFeature, trainingFeatureSet, trainingLabelSet, KNN_K)

