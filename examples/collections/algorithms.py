# -*- encoding: utf-8 -*-
__author__ = 'tao'

import operator


###########################################
# 为容器内的数据进行的排序算法
###########################################

# 为Map/Dict按照value排序
# 按照value的值从大到小排列
coll = {'Seven':7, 'One':1, 'Two':2, 'Three':3, 'Six':6, 'Five':5, 'Four':4}
sortedColl = sorted(coll.iteritems(), key=operator.itemgetter(1), reverse=True)
print sortedColl # [('Seven', 7), ('Six', 6), ('Five', 5), ('Four', 4), ('Three', 3), ('Two', 2), ('One', 1)]
print type(sortedColl)  # 返回的数据类型是list
