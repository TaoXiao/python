# -*- encoding: utf-8 -*-
__author__ = 'tao'

import trees


###################################################################
# tree ： 构建出的决策树
# featLabels : feature的名字的列表，例如 ["Survive", "Fish"]
# testVec：一条测试数据，但是不知道其class
###################################################################
def classify(tree, featLabels, testVec):
    firstStr = tree.keys()[0]
    innerDict = tree[firstStr]
    featIndex = featLabels.index(firstStr)
    for key in innerDict.keys() :
        if key == testVec[featIndex]:
            if type(innerDict[key]).__name__ == 'dict':
                return classify(innerDict[key], featLabels, testVec)
            else:
                return innerDict[key]



# 测试新的数据的预测分类
dataset, labels = trees.createDataset()
decisionTree = trees.createDecisionTree(dataset, labels)
# print decisionTree
# print classify(decisionTree, ["Survive", "Fish"], [1, 0])


dataset, labels = trees.generateDataSet()
decisionTree = trees.createDecisionTree(dataset, labels)
print classify(decisionTree, ['age', 'income', 'student', 'credit_rating'], ['senior',      'medium',   'no',   'excellent'])
